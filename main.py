import enum
from tkinter import *


# sub class
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


# globule variables
groupOfEntry = []
groupOfData = []


# functions
def readNumbers():
    for row in range(0, 9):
        groupOfData.append([])
        for col in range(0, 9):
            input = groupOfEntry[row][col].get()
            dataOfCurrentGrid = None
            if len(input) == 0:
                dataOfCurrentGrid = DataOfEachGrid(0)
            elif input.isnumeric() != True or int(input) > 9 or int(input) < 1:
                print("Enter a number from 1 to 9")
                return False
            elif len(input) == 1 and input.isnumeric():
                dataOfCurrentGrid = DataOfEachGrid(int(input))
            groupOfData[row].append(dataOfCurrentGrid)
    return True


def printData():
    for row in range(0, 9):
        for col in range(0, 9):
            print(str(groupOfData[x][y].numberInGrid), end = " ")


def clicked():
    if readNumbers():
        printData()
        # solve the number place problem
    print("Clicked")


# main start here
window = Tk()
window.title("Number place")
window.geometry("300x300")

for x in range(0, 9):
    groupOfEntry.append([])
    for y in range(0, 9):
        txt = Entry(window, width=3)
        txt.grid(column=x, row=y)
        groupOfEntry[x].append(txt)

solveBtn = Button(window, text="Solve", command=clicked)
solveBtn.grid(column=10, row=10)
window.mainloop()
