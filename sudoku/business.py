
"""Contains the sudoku algorithms.
Assuming you know how to play sudoku, core concepts are:
    * symbols: Possible values to fill in a cell, typically 1..9 plus an invalid symbol for empty cells
    * cell: A place where you can fill in a symbols
    * grid: the 9x9 cells
    * group: cells influencing each other.  Every cell is a member of 3 groups: horizontal, vertical and the 3x3 block
    * dimension2: Number of symbols and size of each group, typically 9
    * worklist: all cells not yet processed
"""

import copy
import random
import math

symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

invalid_symbol = '.'


class Cell:

    def __init__(self, i, j):
        self.at = i, j
        self.choices = copy.copy(symbols)
        self.value = invalid_symbol

    def __repr__(self):
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

    def solve(self):
        if len(self.choices) == 1:
            self.set(self.choices[0])
            return True
        else:
            return False


class Sudoku:

    def groups(self, i, j):
        dimension = int(math.sqrt(self.dimension2))
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
        self.grid = [[Cell(i, j) for j in range(dimension2)]
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
            raise Exception("Invalid symbol")

    def validate(self, i, j):
        return self.grid[i][j].validate()

    def make_solvable(self):
        # Make as many cells blankas possible
        all_cells = reduce(list.__add__, self.grid)
        random.shuffle(all_cells)
        for clean in all_cells:
            child = Sudoku(self.dimension2)
            for cell in all_cells:
                if cell != clean and cell.value <> invalid_symbol:
                    child.set(cell.at[0], cell.at[1], cell.value)
            if child.simple_solve(reduce(list.__add__, child.grid)):
                clean.set(invalid_symbol)
            print "post", child

    def solve(self):
        # Try to find 1 solution to the sudoku, ignoring all others
        # worklist = all cells not yet solved. Random order  so we dont always
        # stabilize on the same solution
        worklist = reduce(list.__add__, self.grid)
        random.shuffle(worklist)
        return self.solve_worklist(worklist)

    def simple_solve(self, worklist):
        # Resolve what we know
        while True:
            newworklist = copy.copy(worklist)
            for cell in worklist:
                if len(cell.choices) == 0:
                    return False
                if cell.solve():
                    worklist.remove(cell)
            if len(worklist) == 0:
                return True
            if len(worklist) == len(newworklist):
                print "no advance", worklist
                return False

    def solve_worklist(self, worklist):
        if self.simple_solve(worklist):
            return True
        # Simple resolution does not work. Take an easy cell an try all
        # possibilities.
        easypos, minlen = 0, len(symbols)
        for i in range(len(worklist)):
            l = len(worklist[i].choices)
            if l < minlen:
                easypos, minlen = i, l

        for choice in worklist[easypos].choices:
            clone = copy.deepcopy(worklist)
            clone[easypos].set(choice)
            if self.solve_worklist(copy.copy(clone)):
                for i in range(len(worklist)):
                    worklist[i].set(clone[i].value)
                return True
        return False
