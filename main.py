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
            print(groupOfData[row][col].currentChoice, end=" ")
        print()
    print()


def clicked():
    if readNumbers():
        printData()
        # solve the number place problem
    print("Clicked")
    if basicBackTrack(0, 0):
        print("Solved")
        for row in range(0, 9):
            for col in range(0, 9):
                setTextInput(groupOfEntry[row][col],
                             str(groupOfData[row][col].currentChoice))
    else:
        print("Failed")


def setTextInput(entry, text):
    entry.delete(0, "end")
    entry.insert(0, text)


def contradictionCheck(row, col):
    for index in range(0, 9):
        if index != row and groupOfData[index][col].currentChoice == groupOfData[row][col].currentChoice:
            groupOfData[row][col].currentChoice = 0
            return False
        if index != col and groupOfData[row][index].currentChoice == groupOfData[row][col].currentChoice:
            groupOfData[row][col].currentChoice = 0
            return False

    leftTop_row = int(row/3)*3
    leftTop_col = int(col/3)*3
    for incOnRow in range(0, 3):
        for incOnCol in range(0, 3):
            currentRow = leftTop_row + incOnRow
            currentCol = leftTop_col + incOnCol
            if currentRow == row and currentCol == col:
                continue
            elif groupOfData[currentRow][currentCol].currentChoice == groupOfData[row][col].currentChoice:
                groupOfData[row][col].currentChoice = 0
                return False

    return True


def basicBackTrack(row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        # print("col == 9")
        col = 0
        row = row + 1
    if groupOfData[row][col].numberInGrid == 0:
        for currentTry in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            printData()
            groupOfData[row][col].currentChoice = currentTry
            if contradictionCheck(row, col):
                if basicBackTrack(row, col + 1):
                    return True
    else:
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
