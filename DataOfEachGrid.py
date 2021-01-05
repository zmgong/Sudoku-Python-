class DataOfEachGrid:
    PotentialChoices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    currentChoice = 0

    def __init__(self, num):
        self.PotentialChoices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.currentChoice = 0
        if num == 0:
            self.numberInGrid = 0
            self.flag = 1 == 1
        elif 9 >= num >= 1:
            self.numberInGrid = num
            self.currentChoice = num
            self.PotentialChoices.remove(num)
            self.flag = 1 == 1
        else:
            self.numberInGrid = num
            self.flag = 1 == 0
