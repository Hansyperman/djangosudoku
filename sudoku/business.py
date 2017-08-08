
"""Contains the sudoku algorithms.
Assuming you know how to play sudoku, core concepts are:
    * symbols: Possible values to fill in a cell, typically 1..9
    * cell: A place where you can fill in a symbols
    * grid: the 9x9 cells
    * group: cells influencing each other.  Every cell is a member of 3 groups: horizontal, vertical and the 3x3 block
    * dimension2: Number of symbols and size of each group
"""

import copy

dimension = 3
dimension2 = dimension * dimension
symbols = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


class Cell:

    def __init__(self):
        self.choices = copy.copy(symbols)
        self.value = None

    def set(symbol):
	self.value=symbol

class Sudoku:

    def __init__(self):
        self.grid = [[Cell() for j in range(dimension2)]
                     for i in range(dimension2)]

    def set(self, i, j, symbol):
        self.grid[i][j].set(symbol)
