#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *  # 导入tkinter库
def on_click():
	label['text']='哈哈'
root = Tk(className='嘿嘿')   # 创建窗口对象的标题
label = Label(root)
label['text'] = 'I love you'
label.pack()
text = StringVar()
text.set('change to what?')
entry = Entry(root)
entry['textvariable'] = text
entry.pack()
button = Button(root)
button['text'] = '点击我'
button['command'] = on_click
button.pack()
root.mainloop()