from tkinter import *
import math


def calculate(rating):
    points = 0
    if rating <= 1500:
        points = 0.22 * 1500 + 14

    elif rating > 1500:
            points = 1511.26/(1+1639.28*math.exp(-0.00412*rating))
    points = int(points)

    # Clearing the entries so we continue to only have 1 number in each entry.
    entry_Points2.delete(0, "end")
    entry_Points3.delete(0, "end")
    entry_Points5.delete(0, "end")

    # Inserts the points into the entrie given the rating
    entry_Points2.insert(0, int(points*0.76))
    entry_Points3.insert(0, int(points * 0.88))
    entry_Points5.insert(0, points)


# Dynamically updating the points when rating is changed
def callback(sv):
    try:
        calculate(int(sv.get()))
    except ValueError:
        print("Only numbers you imbecile")




root = Tk()
sv = StringVar()
# Calls the callback function which updates the points.
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

label_Rating = Label(root, text="Rating")
label_twos = Label(root, text="2v2: ")
label_threes = Label(root, text="3v3: ")
label_fives = Label(root, text="5v5: ")

entry_Rating = Entry(root, textvariable=sv)
entry_Points2 = Entry(root)
entry_Points3 = Entry(root)
entry_Points5 = Entry(root)

# Labels
label_Rating.grid(row=1)
entry_Rating.grid(row=1, column=1)
label_twos.grid(row=0, column=2, padx=10, sticky=E)
label_threes.grid(row=1, column=2, padx=10, sticky=E)
label_fives.grid(row=2, column=2, padx=10, sticky=E)

# Entries
entry_Points2.grid(row=0, column=3)
entry_Points3.grid(row=1, column=3)
entry_Points5.grid(row=2, column=3)

root.mainloop()

