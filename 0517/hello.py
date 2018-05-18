# -*- coding: utf-8 -*-
from Tkinter import *  # 导入Tkinter包的所有内容
import tkMessageBox


# 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
class Application(Frame):  # 从Frame派生一个Application类，这是所有Widget的父容器：
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		# 当用户点击按钮时，触发hello()，
		self.alertButton = Button(self, text='Hello', command=self.hello)
		self.alertButton.pack()

	# 通过self.nameInput.get()获得用户输入的文本后，使用tkMessageBox.showinfo弹出对话框
	def hello(self):
		name = self.nameInput.get() or 'world!'
		tkMessageBox.showinfo('Message', 'Hello, %s' % name)


# 实例化Application，并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('Hello World!')
# 主消息循环
app.mainloop()
