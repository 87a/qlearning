#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:pack_grid_place  文件名称
# DateTime:2021/8/18 17:46  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, ipadx=10, ipady=10)

tk.Label(window, text=1).place(x=10, y=100, anchor='nw')
window.mainloop()