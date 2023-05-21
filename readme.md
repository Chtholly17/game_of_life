# Game of life in Python

## How to run
```
python3 main.py
```
Dependencies:
- pygame
Arguments of Game class:
- `row` - number of rows in the grid
- `col` - number of columns in the grid
- `cells` - the number of cells to be alive at the beginning of the game, their position is random
- `width` - width of each cell
- `height` - height of each cell
- `iterTime` - time between each iteration in seconds
## Game rules
- SPACE :pause/resume
    - when paused: click on a cell to make it alive or dead
- R :reset
- Q or ESC :quit
## Application of Obeserver pattern
- `Game` class is the subject, which is observed by `Iter` and `Environment` classes
- `Iter` class is the observer, which observes the subject and prints the current iteration number
- `Iter` class is also the subject, which is observed by `Environment` class
- `Environment` class is the observer, which observes the subject and prints the current state of the grid
