from tkinter import *


class MyButtons:
    # When function is called the init will automatically be called
    def __init__(self, master): # Master and root is equivalent, ish
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        # Quit breaks the main loop, ie. ending the program.
        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("something something")

root = Tk()
b = MyButtons(root)
root.mainloop()


