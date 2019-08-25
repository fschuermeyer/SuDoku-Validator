'''
SUDOKU VALIDATOR
'''
from collections import OrderedDict


class Validator:

    def __init__(self,grid):
        self.grid = grid

    def createList(self,n):
        return [[] for i in range(0,n)]

    def checkIntegers(self):
        for row in self.grid:
            for i in row:
                if i not in range(1,10):
                    return False
        return True
    
    def checkUnique(self,inputs):
        for i in inputs:
            if len(list(OrderedDict.fromkeys(i))) != 9:
               return False
        return True

    def checkRows(self):
        return self.checkUnique(self.grid)

    def checkDigitsCount(self):
        if len(self.grid) == 9:
            for row in self.grid:
                if len(row) != 9:
                    return False
        else:
            return False
        return True

    def convertToWay(self):
        col = self.createList(9)

        for row in self.grid:
            for i in range(0,9):
                col[i].append(row[i])  

        return col

    def checkCols(self):
        return self.checkUnique(self.convertToWay())

    def convertInGrid(self):
        grids = self.createList(9)
        i = 0

        for row in self.grid:
            if i < 3:
                grids[0].extend((row[0],row[1],row[2]))
                grids[1].extend((row[3],row[4],row[5]))
                grids[2].extend((row[6],row[7],row[8]))

            if i < 6 and i > 2:
                grids[3].extend((row[0],row[1],row[2]))
                grids[4].extend((row[3],row[4],row[5]))
                grids[5].extend((row[6],row[7],row[8]))

            if  i > 5:
                grids[6].extend((row[0],row[1],row[2]))
                grids[7].extend((row[3],row[4],row[5]))
                grids[8].extend((row[6],row[7],row[8]))
            
            i += 1

        return grids

    def checkGrids(self):
        return self.checkUnique(self.convertInGrid())

    def runValidator(self):
        return self.checkDigitsCount() and self.checkIntegers() and self.checkRows() and self.checkCols() and self.checkGrids()

    def shortValidator(self):
        return self.checkRows() and self.checkCols() and self.checkGrids()