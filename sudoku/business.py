
"""Contains the sudoku algorithms.
Assuming you know how to play sudoku, core concepts are:
    * symbols: Possible values to fill in a cell, typically 1..9 plus an invalid symbol for empty cells
    * cell: A place where you can fill in a symbols
    * grid: the 9x9 cells
    * group: cells influencing each other.  Every cell is a member of 3 groups: horizontal, vertical and the 3x3 block
    * dimension2: Number of symbols and size of each group, typically 9
"""

import copy
from math import sqrt

symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

invalid_symbol = '?'


class Cell:

    def __init__(self):
        self.choices = copy.copy(symbols)
        self.value = invalid_symbol

    def __str__(self):
        return self.value + str(self.choices)

    def set(self, symbol):
        self.value = symbol
        if self.value == invalid_symbol:
            return
        # Setting a valid symbol makes it inaccessible in other cells in my
        # groups
        for group in self.groups:
            for cell in group:
                if cell <> self and symbol in cell.choices:
                    cell.choices.remove(symbol)
        # If it was a valid choice, it is the only one
        if self.value in self.choices:
            self.choices = [self.value]
        else:
            self.choices = []

    def validate(self):
        return self.value == invalid_symbol or self.value in self.choices


class Sudoku:

    def groups(self, i, j):
        dimension = int(sqrt(self.dimension2))
        bloki = i / dimension * dimension
        blokj = j / dimension * dimension
        return [
            [self.grid[i][k] for k in range(self.dimension2)],  # horizontal
          [self.grid[k][j] for k in range(self.dimension2)],  # vertical
          [self.grid[k][l]  # 3x3 block
              for k in range(bloki, bloki + dimension) for l in range(blokj, blokj + dimension)]
        ]

    def __init__(self, dimension2):
        self.dimension2 = dimension2
        self.grid = [[Cell() for j in range(dimension2)]
                     for i in range(dimension2)]
        for i in range(dimension2):
            for j in range(dimension2):
                self.grid[i][j].groups = self.groups(i, j)

    def get(self, i, j):
        return self.grid[i][j].value

    def set(self,
            i, j, symbol):
        if symbol in symbols or symbol == invalid_symbol:
            self.grid[i][j].set(symbol)
        else:
            raise "Invalid symbol"

    def validate(self, i, j):
        return self.grid[i][j].validate()
