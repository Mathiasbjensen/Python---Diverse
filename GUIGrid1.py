# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:38:26 2017

@author: Mathias
"""

from tkinter import*

root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root) #Gives a blank field where the user can type something in
entry_2 = Entry(root)

#Now trying with grid instead of pack
label_1.grid(row=0, sticky=E) #top of first column - E is right (north, south, east, west..)
label_2.grid(row=1, sticky=E) #bottom of first column

entry_1.grid(row=0, column=1) #2nd column, so 1
entry_2.grid(row=1, column=1)

#Creating a checkbox

c = Checkbutton(root, text="Keep me logged in")
#Wanting this to take up 2 columns:
c.grid(columnspan=2)


root.mainloop()