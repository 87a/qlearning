#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:messagebox  文件名称
# DateTime:2021/8/18 17:13  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def hit_me():
    # tk.messagebox.showinfo(title='Hi', message='hahahaha')
    # tk.messagebox.showwarning(title='Hi', message='nononono')
    # tk.messagebox.showerror(title='Hi', message='No!! never')
    # print(tk.messagebox.askquestion(title='Hi', message='hahaha'))  # return yes or no
    # print(tk.messagebox.askyesno(title='Hi', message='hahaha'))  # return Ture or False
    # print(tk.messagebox.askretrycancel(title='Hi', message='hahaha'))  # return Ture or False
    print(tk.messagebox.askokcancel(title='Hi', message='hahaha'))  # return Ture or False

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()
