from tkinter import *
import re
import math
import numpy as np

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

#price = " |   $499.99   | "
#print(re.findall(r"[$](\w+)",price))

# name = "sofffie"
#
# print(name.count('f'))

A = np.array([[1,2,6,10],[3,7,7,13],[7,9,11,14]])

print(np.size(A,axis=0))
print(np.size(A,axis=1))

print(np.shape(A))
print(A)
