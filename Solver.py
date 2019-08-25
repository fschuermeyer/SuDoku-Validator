from Validator import Validator as v
from copy import deepcopy as deep
import random
import sys

# It's not Finish Jet 

class Solver:

    def __init__(self,grid,possibleValues = range(1,10),placeholder = 0):
        self.gridList = list()
        self.debug = False
        self.toSolve = self.checkFormatGrid(grid)
        self.possibleValues = possibleValues
        self.placeholder = placeholder

        print('Start Sodoku Solver')

    def posInGrid(self):
        self.IdentWrapper(v(self.toSolve).convertInGrid(),"grids")  

    def posInRow(self):
        self.IdentWrapper(self.toSolve,"row")  

    def posInCol(self):
        self.IdentWrapper(v(self.toSolve).convertToWay(),"col")


    def IdentWrapper(self,grid,name):
        c = 0

        for x in grid:
            t = self.isNotinRange(x)
            if len(t) > 0:
                grid = self.inputPossibleValues(t,c,grid)

            c += 1
            
        if name == 'col':
            self.storageGrids(name,v(grid).convertToWay())
        elif name == 'grids':
            self.storageGrids(name,v(grid).convertInGrid())
        else:
            self.storageGrids(name,grid)
         


    def isNotinRange(self,elm):
        values = list(self.possibleValues)
    
        for b in elm:
            if b in values:
                values.remove(b)

        return values


    def checkForPlaceholder(self):
        c = 0
        for row in self.toSolve:
            for n in row:
                if n == self.placeholder:
                    c += 1
        return c


    def checkFormatGrid(self,grid):
        
        if(len(grid) != 9):
            self.fireInvalidGrid("Not 9 Rows in the Grid wrong Input")
        else:
            for c in grid:
                if(len(c) != 9):
                    self.fireInvalidGrid("Not 9 Numbers or Placeholder in a Row wrong Input")
        return grid

   
    def inputPossibleValues(self,t,c,copy):
        for index,item in enumerate(copy[c]):
            if copy[c][index] == 0:
                copy[c][index] = t
            elif type(copy[c][index]) is not int:
                copy[c][index] = t
        
        return copy

    def getSolvedGrid(self):

        self.posInCol()
        self.posInRow()
        self.posInGrid()
        self.compareAllPossibleGrids()


        self.createListOfGrids()

    def raoRow(self,items,r):
        for itemIndex,item in enumerate(items):
            if type(item) is list:
                if r in items[itemIndex]:
                    items[itemIndex].remove(r)
        return items

    def raoCol(self,grid,colN,r):
        for rowIndex,row in enumerate(grid):
            for nIndex,n in enumerate(row):
                if colN == nIndex:
                    if type(grid[rowIndex][nIndex]) is list:
                        if r in grid[rowIndex][nIndex]:
                            grid[rowIndex][nIndex].remove(r)
        return grid


    def checkForColRow(self,grid,nIndex,rowIndex,n):
        random.shuffle(n)
        lk = False
        jk = False
        x = 1

        if len(n) == 0:
            n = self.getGridByName('pos')[rowIndex][nIndex]

        while any([jk,lk]) or x == 1:
            x += 1
            if any([jk,lk]):
                random.shuffle(n)
                lk = False
                jk = False

            for xb in grid:
                if type(xb[nIndex]) is not list:
                        if n[0] == xb[nIndex]:
                            lk = True

            for cz in grid[rowIndex]:
                if type(cz) is int:
                    if cz == n[0]:
                        jk = True
            
            if x > 30:
                lk = False
                jk = False

        
        return n


    def createListOfGrids(self):
        b = 0
        exWrong = False
        oldGrid = list()
        Indikator = 0
        workerGrid = list()

        while True:
            workerGrid = self.getGridByName("pos")

            for rowIndex,row in enumerate(workerGrid):
                for nIndex,n in enumerate(row):
                    if type(n) is list and exWrong is False:
                        n = self.checkForColRow(workerGrid,nIndex,rowIndex,n)
                
                        try:
                            workerGrid[rowIndex][nIndex] = n[0]
                            workerGrid[rowIndex] = self.raoRow(workerGrid[rowIndex],n[0])
                            workerGrid = self.raoCol(workerGrid,nIndex,n[0])
                        except:
                            exWrong = True
                                        
            if workerGrid in oldGrid or exWrong:
                if b == 100000000:
                    print("Out of Run")
                    print(len(oldGrid))
                    break
                exWrong = False
            else:    
                oldGrid.append(deep(workerGrid))

                if v(workerGrid).shortValidator():
                    print("---------------------------------")
                    print(self.prettyPrintGrid(workerGrid,"Valid Result"))
                    print("Test Runs: " + str(b))
                    print("Grids: " + str(len(oldGrid)))
                    self.count = b
                    print("---------------------------------")
                    break
            
                b += 1
            Indikator += 1

    def getCount(self):
        c = self.count
        self.count = 0
        return c
           
    def compareAllPossibleGrids(self):
        compared = list()
        
        for x in range(1,10):
            compared.append(list())
        
        for gridIndex,grid in enumerate(self.gridList):
            gridElm = grid[1]

            for rowIndex,row in enumerate(gridElm):
                for nIndex,n in enumerate(row):
                    if type(n) is int:
                        if gridIndex == 0:
                            compared[rowIndex].append(n)
                        else:
                            compared[rowIndex][nIndex] = n
                    else:
                        try:
                            uniq = []

                            if(type(compared[rowIndex][nIndex]) is int):
                                newList = []
                                newList.append(compared[rowIndex][nIndex])
                                compared[rowIndex][nIndex] = newList
                            else:
                                compared[rowIndex][nIndex].extend(n)
                            un = [uniq.append(x) for x in compared[rowIndex][nIndex] if x not in uniq]
                            
                            if len(uniq) == 1:
                                uniq = uniq[0]

                            compared[rowIndex][nIndex] = uniq
                        except IndexError:
                            compared[rowIndex].append(n)
            

        self.storageGrids("pos",compared)

    def storageGrids(self,msg,grid,debug = False):
        if debug or self.debug:
            self.prettyPrintGrid(grid,msg)

        self.gridList.append((msg,grid))

    def getGridByName(self,name):
        for x in self.gridList:
            if x[0] == name:
                return deep(x[1])
        
        return False

    def getPlacedNumbers(self):
        pass

    def fireInvalidGrid(self,msg):
        raise InvalidGrid(msg)

    def prettyPrintGrid(self,grid,name):
    
        print(name)
        print("---")
        for c in grid:
            print(c)
        print("---")
    
class InvalidGrid(Exception):
    def __init__(self,msg):
        self.message = msg
    
    def __str__(self):
        return self.message