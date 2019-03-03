'''
SUDOKU VALIDATOR
'''
from collections import OrderedDict


class SuDokuValidator:

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
        if self.checkDigitsCount() & self.checkIntegers() & self.checkRows()  & self.checkCols() & self.checkGrids():
            print('Valid')
        else:
            print('Not Valid')

    


# Valide Grid
valid = [
    [4,8,3,9,2,1,6,5,7], # ROW
    [9,6,7,3,4,5,8,2,1],
    [2,5,1,8,7,6,4,9,3],
    [5,4,8,1,3,2,9,7,6],
    [7,2,9,5,6,4,1,3,8],
    [1,3,6,7,9,8,2,4,5],
    [3,7,2,6,8,9,5,1,4],
    [8,1,4,2,5,3,7,6,9],
    [6,9,5,4,1,7,3,8,2]
    # COL
]

# Invalid Grid 
invalidOne = [
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9]
]

# Invalid Grid 
invalidSecond = [
    [0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,9],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,1,5,0,1,0,3,0,0]
]

TheValidator = SuDokuValidator(valid)
TheValidator.runValidator()