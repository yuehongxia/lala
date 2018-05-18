#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 引入tkinter工具包
from tkinter import *
def haha():
	print('你好！')

win = Tk() # 定义一个窗体
win.geometry('400x200') # 定义窗体大小

btn = Button(win,text='点击我',command=haha)
btn.pack(expand=YES,fill=BOTH)# 将按钮pack，充满整个窗体
mainloop()# 进入主循环，程序运行