from tkinter import *


def doNothing():
    print("bla bla bla...")

root = Tk()

menu = Menu(root)
root.config(menu=menu) # Configuring menu

subMenu = Menu(menu, tearoff=0) # tearoff removes the dashed line (------------)
# dropdownmenu --> cascading
menu.add_cascade(label="File", menu=subMenu) # Creates a file button that has dropdown functionality
# adding stuff to the dropdown menu
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
# Separator is the line between dropdown menu items
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

#Making another item, drop down bracket thing
editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()