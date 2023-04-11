# _*_ coding : utf-8 _*_
# @Time : 2023/4/11 17:27
# @Author : Black
# @File : quiz_gui.py
# @Project : EasyRecite


import tkinter as tk
from tkinter import font
import random
from questions_answers import *


class QuizGUI:
    def __init__(self, questions, answers):
        self.submit_button = None
        self.answer_entry = None
        self.answer_label = None
        self.question_label = None
        self.questions = questions
        self.answers = answers
        self.used_questions = []
        self.current_question = None
        self.current_answer = None
        self.root = tk.Tk()
        self.root.title('EasyRecite')
        self.root.geometry('800x600')
        self.create_widgets()
        self.waiting_for_answer = False

    def create_widgets(self):
        # 创建问题标签和答案标签
        self.question_label = tk.Label(self.root, text='', font=font.Font(size=16))
        self.question_label.pack(pady=40)
        self.answer_label = tk.Label(self.root, text='', font=font.Font(size=16))
        self.answer_label.pack(pady=40)

        # 创建输入框和按钮
        self.answer_entry = tk.Entry(self.root, font=font.Font(size=16), width=50)
        self.answer_entry.pack(pady=40)
        self.answer_entry.bind('<Return>', self.check_answer)
        self.submit_button = tk.Button(self.root, text='确认', font=font.Font(size=16), command=self.check_answer)
        self.submit_button.pack(pady=40)

        # 随机选择问题和答案
        self.random_question()
        self.show_question()

    def random_question(self):
        # 如果还有未使用的问题，随机选择一个问题
        unused_questions = set(range(len(self.questions))) - set(self.used_questions)
        if unused_questions:
            self.current_question = random.choice(list(unused_questions))
            self.used_questions.append(self.current_question)
            self.current_answer = self.answers[self.current_question]
        # 如果所有问题都已使用，提示完成
        else:
            self.current_question = None
            self.current_answer = None
            self.question_label.config(text='恭喜你已经回答完所有问题！')
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)

    def show_question(self):
        # 如果当前有问题，显示问题，否则提示完成
        if self.current_question is not None:
            self.question_label.config(text=self.questions[self.current_question], wraplength=700)
            self.answer_label.config(text='')
        else:
            self.question_label.config(text='恭喜你已经回答完所有问题！')

    def check_answer(self, event=None):
        if self.waiting_for_answer:
            self.random_question()
            self.show_question()
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.config(state=tk.NORMAL)
            self.submit_button.config(state=tk.NORMAL)
            self.waiting_for_answer = False
        else:
            if self.answer_entry.get().strip() == self.current_answer:
                self.answer_label.config(text='回答正确！', fg='red')
            else:
                self.answer_label.config(text=f'宝贝加油！{self.current_answer}', fg='red', wraplength=700)
                # self.answer_entry.config(state=tk.DISABLED)
                # self.submit_button.config(state=tk.DISABLED)
                self.waiting_for_answer = True


if __name__ == '__main__':
    quiz_gui = QuizGUI(questions, answers)
    quiz_gui.root.mainloop()
