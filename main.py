from tkinter import *

# globule variables
import BackTrack
from DataOfEachGrid import DataOfEachGrid

groupOfEntry = []
board = []


# functions
def readNumbers():
    while len(board) != 0:
        board.clear()
    for row in range(0, 9):
        board.append([])
        for col in range(0, 9):
            inputStr = groupOfEntry[row][col].get()
            if len(inputStr) == 0:
                board[row].append(0)
            elif inputStr.isnumeric() is not True or int(inputStr) > 9 or int(inputStr) < 1:
                print("Enter a number from 1 to 9")
                return False
            elif len(inputStr) == 1 and inputStr.isnumeric():
                board[row].append(int(inputStr))
    return True


def printData():
    for row in range(0, 9):
        for col in range(0, 9):
            print(board[row][col], end=" ")
        print()
    print()


def clicked():
    if readNumbers():
        printData()
        # solve the number place problem
    print("Clicked")
    result = BackTrack.backTrackWithArcConsCheck(board)
    if result is False:
        print("Failed")
    else:
        print("Solved")
        for row in range(0, 9):
            for col in range(0, 9):
                setTextInput(groupOfEntry[row][col],
                             str(result[row][col].currentChoice))


def setTextInput(entry, text):
    entry.delete(0, "end")
    entry.insert(0, text)


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
