'''
    @brief: This file contains the main game loop
'''
from environment import Environment
from iter import Iter
import pygame

class Game:
    ''' game class for the game of life
    '''
    
    def __init__(self,row,col,iterTime = 0.1,cells = 10, width = 10,height = 10) -> None:
        ''' constructor for the game class
        Args:
            row: number of rows in the grid
            col: number of columns in the grid
            cells: number of cells in the grid at the start
            width: width of each cell
            height: height of each cell
        '''
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.state = 'pause'
        self.initCells = cells
        self.environment = Environment(row,col,self.initCells)
        self.iter = Iter(iterTime)
        self.iter.attach(self.environment)
            
    
        
    def notifyIter(self,type) -> None:
        ''' notifies the iter'''
        self.iter.update(type)
        
    def notifyEnvironment(self,row = 0,col = 0,type = "update") -> None:
        ''' notifies the environment'''
        self.environment.update(type,row,col)
        
    def update(self) -> None:
        ''' updates the game'''
        # check if the game state is run
        if self.state == 'run':
            # update the game
            self.notifyIter("iteration")
        # update the screen
        pygame.display.update()
            
    def draw(self, screen) -> None:
        ''' draws the grid on the screen'''
        # update the screen, if the grid is alive, draw a white rectangle, else draw a black rectangle
        for row in range(self.row):
            for col in range(self.col):
                if self.environment.getAlive(row,col) == True:
                    # print(self.environment.getAlive(row,col))
                    # print(row,col)
                    pygame.draw.rect(screen, (255, 255, 255), (col * self.width, row * self.height, self.width, self.height))
                else:
                    
                    pygame.draw.rect(screen, (0, 0, 0), (col * self.width, row * self.height, self.width, self.height))
    
    def updateCoordinates(self, x: int, y: int) -> None:
        ''' updates cell alive status based on the coordinates'''
        # get the row and column index of the cell
        row = y // self.height
        col = x // self.width
        # update the environment
        self.notifyEnvironment(row,col,"update")
        
    def reset(self) -> None:
        ''' resets the game'''
        # set the game state to pause
        print("game reset")
        self.state = 'pause'
        # reset the game
        self.notifyEnvironment(type = "reset")
        self.notifyIter(type = "reset")
        
    def changeState(self) -> None:
        ''' changes the game state'''
        # check if the game state is run
        if self.state == 'run':
            # set the game state to pause
            self.state = 'pause'
        else:
            # set the game state to run
            self.state = 'run'
        
    def run(self):
        ''' runs the game'''
        # initialize pygame
        pygame.init()  
        # set the screen size
        screen = pygame.display.set_mode((self.width*self.col, self.height*self.row))
        # set the title of the window
        pygame.display.set_caption('Game of Life')
        screen.fill((0,0,0))
        # main game loop
        while True:
            # get the events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and self.state == 'pause':
                    # get the position of the mouse
                    x, y = pygame.mouse.get_pos()
                    self.updateCoordinates(x,y)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # pause or run the game
                        self.changeState()
                    elif event.key == pygame.K_r:
                        # reset the game
                        self.reset()
                    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        # quit the game
                        pygame.quit()
                        exit()
            # update the game
            self.update()
            self.draw(screen)
