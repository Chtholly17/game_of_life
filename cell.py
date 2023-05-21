'''
    @brief: Cell class for the game of life
'''

class Cell:
    ''' cell class for the game of life
    Attributes:
        alive: boolean value to indicate if the cell is alive or not
        neighbours: list of neighbours of the cell
    '''
    
    def __init__(self) -> None:
        ''' constructor for the cell class'''
        self.alive = False
        self.neighbours = []
    
    def add_neighbour(self, cell) -> None:
        ''' adds a neighbour to the cell
        Args:
            cell: cell object to be added as a neighbour
        '''
        self.neighbours.append(cell)
        
    def get_neighbours(self) -> list:
        ''' returns the list of neighbours of the cell
        Returns:
            list of neighbours of the cell
        '''
        return self.neighbours
    
    def get_alive(self) -> bool:
        ''' returns the alive status of the cell
        Returns:
            boolean value indicating if the cell is alive or not
        '''
        return self.alive
    
    def set_alive(self, alive: bool) -> None:
        ''' sets the alive status of the cell
        Args:
            alive: boolean value to set the alive status of the cell
        '''
        self.alive = alive
        
    def update(self) -> None:
        ''' updates the alive status of the cell based on the number of alive neighbours'''
        alive_neighbours = 0
        for neighbour in self.neighbours:
            if neighbour.get_alive():
                alive_neighbours += 1
        
        if self.alive:
            if alive_neighbours < 2 or alive_neighbours > 3:
                self.alive = False
        else:
            if alive_neighbours == 3:
                self.alive = True

        