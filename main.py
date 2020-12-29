import enum
from tkinter import *


class DataOfEachGrid:
    PotentialChoices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    currentChoice = 0

    def __init__(self, num):
        if num == 0:
            self.numberInGrid = 0
            self.flag = 1 == 1
        elif 9 >= num >= 1:
            self.numberInGrid = num
            self.PotentialChoices.remove(num)
            self.flag = 1 == 1
        else:
            self.numberInGrid = num
            self.flag = 1 == 0


def readNumbers():
    return 0


window = Tk()
window.title("Number place")
window.geometry("300x300")

grids = []
for x in range(0, 9):
    grids.append([])
    for y in range(0, 9):
        txt = Entry(window, width=3)
        txt.grid(column=x, row=y)
        grids[x].append(txt)


def clicked():
    s = grids[0][0].get()
    print(s)


solveBtn = Button(window, text="Solve", command=clicked)
solveBtn.grid(column=10, row=10)
window.mainloop()
