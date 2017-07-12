# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:21:22 2017

@author: Mathias
"""

from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Making buttons, ish

#Making 3 buttons in the topFrame.
button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
#and 1 in the bottomFrame
button4 = Button(bottomFrame, text="Button 4", fg="purple")


#Now we have to pack them in.

#Buttons by default appear on top of eachother, hence the parameters to not have it like that.
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()