#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import * # 导入工具包
__author__ = 'fyby'
class App:
	def __init__(self,master):# 构造函数里传入一个父组件（master），创建一个Frame组件并显示
		frame = Frame(master)
		frame.pack()
		#创建两个button,并作为frame的一部分
		self.button = Button(frame,text='QUIT',fg="red",command=frame.quit)
		self.button.pack(side=RIGHT)# 放置在左边
		self.hi_there = Button(frame,text="hello",command=self.hehe)
		self.hi_there.pack(side=RIGHT)

	def hehe(self):
		print "哈哈啊！"

win = Tk()
app = App(win)
win.mainloop()
