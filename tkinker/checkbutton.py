#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:checkbutton  文件名称
# DateTime:2021/8/18 14:54  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()
var1 = tk.IntVar()
var2 = tk.IntVar()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')


c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0
                    , command=print_selection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0
                    , command=print_selection)
c1.pack()
c2.pack()

window.mainloop()
