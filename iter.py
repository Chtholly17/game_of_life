'''
    @brief: This file is used to create a Iter for the game
'''

import time

class Iter:
    ''' timer class for the game of life, used to update the game at regular intervals
    Attributes:
        interval: time interval between each update
    '''
    def __init__(self, interval: float) -> None:
        ''' constructor for the timer class
        Args:
            interval: time interval between each update
            iteration: number of iterations
            observers: list of observers
        '''
        self.interval = interval    
        self.iteration = 0
        self.observers = []
        
    def get_iteration(self) -> int:
        ''' returns the number of iterations
        Returns:
            number of iterations
        '''
        return self.iteration
        
    def attach(self, observer) -> None:
        ''' attaches an observer to the timer
        Args:
            observer: observer to be attached
        '''
        self.observers.append(observer)
        
    def detach(self, observer) -> None:
        ''' detaches an observer from the timer
        Args:
            observer: observer to be detached
        '''
        self.observers.remove(observer)
        
    def notify(self) -> None:
        ''' notifies all the observers'''
        for observer in self.observers:
            observer.update()
        
    def update(self, type = "iteration") -> None:
        ''' updates the game at regular intervals'''
        if type == "iteration":
            self.iteration += 1
            print("Iteration: ",self.iteration)
            time.sleep(self.interval)
            self.notify()

        elif type == "reset": 
            self.iteration = 0