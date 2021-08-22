#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:entry_text  文件名称
# DateTime:2021/8/18 10:33  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

e = tk.Entry(window, show='*')
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=15, height=2,
               command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
