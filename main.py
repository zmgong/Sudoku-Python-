from tkinter import *


# globule variables
from DataOfEachGrid import DataOfEachGrid

groupOfEntry = []
groupOfData = []


# functions
def readNumbers():
    while len(groupOfData) != 0:
        groupOfData.clear()
    for row in range(0, 9):
        groupOfData.append([])
        for col in range(0, 9):
            inputStr = groupOfEntry[row][col].get()
            dataOfCurrentGrid = None
            if len(inputStr) == 0:
                dataOfCurrentGrid = DataOfEachGrid(0)
            elif inputStr.isnumeric() != True or int(inputStr) > 9 or int(inputStr) < 1:
                print("Enter a number from 1 to 9")
                return False
            elif len(inputStr) == 1 and inputStr.isnumeric():
                dataOfCurrentGrid = DataOfEachGrid(int(inputStr))
            groupOfData[row].append(dataOfCurrentGrid)
    return True


def printData():
    for row in range(0, 9):
        for col in range(0, 9):
            print(groupOfData[row][col].numberInGrid, end = " ")
        print()


def clicked():
    if readNumbers():
        printData()
        # solve the number place problem
    print("Clicked")
    if basicBackTrack(0, 0):
        print("Solved")
        for x in range(0, 9):
            for y in range(0, 9):
                setTextInput(groupOfEntry[x][y],
                             str(groupOfData[x][y].currentChoice))


def setTextInput(entry, text):
    entry.delete(0,"end")
    entry.insert(0, text)


def contradictionCheck(row, col):
    for index in range(0, 9):
        if index != row and groupOfData[x][col].currentChoice == groupOfData[row][col].currentChoice:
            return False
        if index != col and groupOfData[row][x].currentChoice == groupOfData[row][col].currentChoice:
            return False

    downRight_row = row + 1
    downRight_col = col + 1
    while 0 <= downRight_row <= 8 and 0 <= downRight_col <= 8:
        if groupOfData[downRight_row][downRight_col].currentChoice == groupOfData[row][col].currentChoice:
            return False
        downRight_row = downRight_row + 1
        downRight_col = downRight_col + 1

    upRight_row = row - 1
    upRight_col = col + 1
    while 0 <= upRight_row <= 8 and 0 <= upRight_col <= 8:
        if groupOfData[upRight_row][upRight_col].currentChoice == groupOfData[row][col].currentChoice:
            return False
        upRight_row = upRight_row - 1
        upRight_col = upRight_col + 1

    downLeft_row = row + 1
    downLeft_col = col - 1
    while 0 <= downLeft_row <= 8 and 0 <= downLeft_col <= 8:
        if groupOfData[downLeft_row][downLeft_col].currentChoice == groupOfData[row][col].currentChoice:
            return False
        downLeft_row = downLeft_row + 1
        downLeft_col = downLeft_col - 1

    upLeft_row = row - 1
    upLeft_col = col - 1
    while 0 <= upLeft_row <= 8 and 0 <= upLeft_col <= 8:
        if groupOfData[upLeft_row][upLeft_col].currentChoice == groupOfData[row][col].currentChoice:
            return False
        upLeft_row = upLeft_row - 1
        upLeft_col = upLeft_col - 1


def basicBackTrack(row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        col = 0
        row = row + 1
    if groupOfData[row][col].numberInGrid != 0:
        for currentTry in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            groupOfData[row][col].currentChoice = currentTry
            if contradictionCheck(row, col):
                if basicBackTrack(row, col + 1):
                    return True




# main start here
window = Tk()
window.title("Number place")
window.geometry("300x300")

for x in range(0, 9):
    groupOfEntry.append([])
    for y in range(0, 9):
        txt = Entry(window, width=3)
        txt.grid(column=y, row=x)
        groupOfEntry[x].append(txt)

solveBtn = Button(window, text="Solve", command=clicked)
solveBtn.grid(column=10, row=10)
window.mainloop()
