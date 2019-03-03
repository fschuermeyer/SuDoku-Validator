'''
SUDOKU VALIDATOR
'''
from collections import OrderedDict


class SuDoku:

    def __init__(self,grid):
        self.grid = grid

    def checkIntegers(self):
        for row in self.grid:
            for i in row:
                if i in range(1,10):
                    pass
                else:
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

    def checkCols(self):
        col = [[],[],[],[],[],[],[],[],[]]

        for row in self.grid:
            for i in range(0,9):
                col[i].append(row[i]) 
            
        return self.checkUnique(col)

    def checkGrids(self):
        grids = [[],[],[],[],[],[],[],[],[]]
        i = 0

        for row in self.grid:
            if i < 3:
                grids[0].append(row[0])
                grids[0].append(row[1])
                grids[0].append(row[2])

                grids[1].append(row[3])
                grids[1].append(row[4])
                grids[1].append(row[5])

                grids[2].append(row[6])
                grids[2].append(row[7])
                grids[2].append(row[8])

            if i < 6 and i > 2:
                grids[3].append(row[0])
                grids[3].append(row[1])
                grids[3].append(row[2])

                grids[4].append(row[3])
                grids[4].append(row[4])
                grids[4].append(row[5])

                grids[5].append(row[6])
                grids[5].append(row[7])
                grids[5].append(row[8])

            if  i > 5:
                grids[6].append(row[0])
                grids[6].append(row[1])
                grids[6].append(row[2])

                grids[7].append(row[3])
                grids[7].append(row[4])
                grids[7].append(row[5])

                grids[8].append(row[6])
                grids[8].append(row[7])
                grids[8].append(row[8])

            i += 1
 
        return self.checkUnique(grids)

    def runValidator(self):
        if self.checkDigitsCount() and self.checkIntegers() and self.checkRows() and self.checkCols() and self.checkGrids():
            print('Valid')
        else:
            print('Not Valid')

    

