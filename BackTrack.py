from DataOfEachGrid import DataOfEachGrid
import bisect

groupOfData = []
result = []


def readFromBoard(board):
    while len(groupOfData) != 0:
        groupOfData.clear()
    for row in range(0, 9):
        groupOfData.append([])
        for col in range(0, 9):
            inputOfThisGrid = board[row][col]
            dataOfCurrentGrid = None
            if inputOfThisGrid == 0:
                dataOfCurrentGrid = DataOfEachGrid(0)
            elif inputOfThisGrid > 9 or inputOfThisGrid < 1:
                print("Enter a number from 1 to 9")
                return False
            else:
                dataOfCurrentGrid = DataOfEachGrid(inputOfThisGrid)
            groupOfData[row].append(dataOfCurrentGrid)
    return True


def contradictionCheck(row, col):
    for index in range(0, 9):
        if index != row and groupOfData[index][col].currentChoice == groupOfData[row][col].currentChoice:
            groupOfData[row][col].currentChoice = 0
            return False
        if index != col and groupOfData[row][index].currentChoice == groupOfData[row][col].currentChoice:
            groupOfData[row][col].currentChoice = 0
            return False

    leftTop_row = int(row / 3) * 3
    leftTop_col = int(col / 3) * 3
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


# This is the very basic backtrack solution.
def basicBackTrackRec(row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        # print("col == 9")
        col = 0
        row = row + 1
    if groupOfData[row][col].numberInGrid == 0:
        for currentTry in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            groupOfData[row][col].currentChoice = currentTry
            if contradictionCheck(row, col):
                if basicBackTrackRec(row, col + 1):
                    return True
    else:
        if basicBackTrackRec(row, col + 1):
            return True
    return False


def basicBackTrack(board):
    if readFromBoard(board) and basicBackTrackRec(0, 0):
        return groupOfData
    else:
        return False


# backTrack with forward check.
def removeKeyFromRowColAndSubGrids(row, col, key):
    listOfRow = []
    listOfCol = []
    for index in range(0, 9):
        if index != row and key in groupOfData[index][col].PotentialChoices:
            groupOfData[index][col].PotentialChoices.remove(key)
            listOfRow.append(index)
            listOfCol.append(col)
        if index != col and key in groupOfData[row][index].PotentialChoices:
            groupOfData[row][index].PotentialChoices.remove(key)
            listOfRow.append(row)
            listOfCol.append(index)

        leftTop_row = int(row / 3) * 3
        leftTop_col = int(col / 3) * 3
        for incOnRow in range(0, 3):
            for incOnCol in range(0, 3):
                currentRow = leftTop_row + incOnRow
                currentCol = leftTop_col + incOnCol
                if currentRow == row and currentCol == col:
                    continue
                elif key in groupOfData[currentRow][currentCol].PotentialChoices:
                    groupOfData[currentRow][currentCol].PotentialChoices.remove(key)
                    listOfRow.append(currentRow)
                    listOfCol.append(currentCol)
    return [listOfRow, listOfCol]


def addKeyBackToRowColAndSubGrids(listOfRow, listOfCol, key):
    if len(listOfRow) == len(listOfCol):
        for i in range(0, len(listOfRow)):
            bisect.insort(groupOfData[listOfRow[i]][listOfCol[i]].PotentialChoices, key)
        return True
    else:
        return False




def backTrackWithForwardRec(row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        # print("col == 9")
        col = 0
        row = row + 1
    if groupOfData[row][col].numberInGrid == 0:
        for currentTry in groupOfData[row][col].PotentialChoices:
            groupOfData[row][col].currentChoice = currentTry
            rowIndexAndColIndex = removeKeyFromRowColAndSubGrids(row, col, currentTry)
            if contradictionCheck(row, col):
                if backTrackWithForwardRec(row, col + 1):
                    return True
            if addKeyBackToRowColAndSubGrids(rowIndexAndColIndex[0], rowIndexAndColIndex[1], currentTry) is False:
                print("ERROR!!!")
                return False
    else:
        if backTrackWithForwardRec(row, col + 1):
            return True
    return False


def backTrackWithForward(board):
    if readFromBoard(board) and backTrackWithForwardRec(0, 0):
        return groupOfData
    else:
        return False


# Backtrack with arc consistency check


# If any grid lost any potential value, call this function to check it's neighbour.
# In this progress, if any neighbour lost any potential value, check the neighbour's neighbour too.
