'''
    @brief: This file contains the grid class
'''

from cell import Cell
import random

class Environment:
    ''' grid class for the game of life
    Attributes:
        rows: number of rows in the grid
        cols: number of columns in the grid
        grid: 2D list of cells
    '''
    
    def __init__(self, rows: int, cols: int, cells:int) -> None:
        ''' constructor for the grid class
        Args:
            rows: number of rows in the grid
            cols: number of columns in the grid
            cells: number of cells in the grid at the start
        '''
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        # randomly set the alive status of the cells
        self.cells = cells
        self.resetCells()
        self.__set_neighbours()
    
    def __set_neighbours(self) -> None:
        ''' sets the neighbours of each cell in the grid'''
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k >= 0 and k < self.rows and l >= 0 and l < self.cols:
                            if k != i or l != j:
                                self.grid[i][j].add_neighbour(self.grid[k][l])
                                
    def setAlive(self, row: int, col: int, alive: bool) -> None:
        ''' sets the alive status of a cell in the grid
        Args:
            row: row index of the cell
            col: column index of the cell
            alive: boolean value to set the alive status of the cell
        '''
        self.grid[row][col].set_alive(alive)
        
    def getAlive(self, row: int, col: int) -> bool:
        ''' returns the alive status of a cell in the grid
        Args:
            row: row index of the cell
            col: column index of the cell
        Returns:
            boolean value indicating if the cell is alive or not
        '''
        return self.grid[row][col].get_alive()
    
    def resetCells(self) -> None:
        for i in range(self.rows):
                for j in range(self.cols):
                    self.setAlive(i,j,False)
        # randomly set the alive status of the cells
        for _ in range(self.cells):
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.cols-1)
            self.setAlive(row,col,True)
        
    def update(self,type = "iter", row = 0, col = 0) -> None:
        ''' updates the alive status of each cell in the grid'''
        if type == "iter": # update all cells
            for i in range(self.rows):
                for j in range(self.cols):
                    self.grid[i][j].update()
        elif type == "update": # update a single cell
            if self.getAlive(row,col):
                self.setAlive(row,col,False)
            else:
                self.setAlive(row,col,True)
        elif type == "reset": # clear the grid
            self.resetCells()
                
                
    