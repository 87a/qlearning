#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:scale  文件名称
# DateTime:2021/8/18 11:18  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, width=20, bg='yellow', text='empty')
l.pack()


def print_selection(v):
    l.config(text='you have select ' + v)


s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=1, tickinterval=3, resolution=0.01,
             command=print_selection)
s.pack()

window.mainloop()
