# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:31:13 2017

@author: Mathias
"""

from tkinter import *

root = Tk()

#bg = background, fg = foreground.

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

#The pack parameter makes two and three fit the "bars" no matter how much you stretch the window,  ie. dynamic.

root.mainloop()