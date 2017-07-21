from tkinter import *
import re

# def callback(sv):
#     print(sv.get())
#
# root = Tk()
# sv = StringVar()
# sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
# e = Entry(root, textvariable=sv)
# e.pack()
# root.mainloop()

#my_string = "hello python world , i'm a beginner world, skod"
#print(my_string.split("world",1)[1])

price = " |   $499.99   | "
print(re.findall(r"[$](\w+)",price))


