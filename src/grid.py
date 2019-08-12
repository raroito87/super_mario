import copy

from src import Cell, CellType

class Grid:
    def __init__(self, grid):
        # initialize the board
        self.board = grid

    def get_size(self):
        # it is always square
        return [len(self.board), len(self.board)]

    def at(self, pos):
        return self.board[pos[0]][pos[1]]

    def is_valid_point(self, pos):
        sz = self.get_size()
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < sz[0] and pos[1] < sz[1]

    def print_grid(self):
        for row in self.board:
            for cell in row:
                print(f'[{cell.pos} {cell.type} {cell.count}]      ', end = '')
            print(' ')

    def print_grid_extended(self):
        for row in self.board:
            for cell in row:
                print(f'[{cell.pos} {cell.type} {cell.count} {len(cell.paths_from)}]      ', end = '')
            print(' ')
