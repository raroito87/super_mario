import copy

from src import Cell, CellType

class Grid:
    def __init__(self, s_x, s_y):
        # initialize the board
        self.board = [[Cell(type = CellType.free, pos=[ix,iy]) for iy in range(s_y)] for ix in range(s_x)]
        self. initialized = False

    def get_size(self):
        return [len(self.board), len(self.board[0])]

    def at(self, pos):
        return self.board[pos[0]][pos[1]]

    def clone(self):
        return Grid(copy.deepcopy(self.board))

    def clear_count(self, count):
        for o in self.board:
            for i in o:
                i.count = count
                i.path_from = None

    def is_valid_point(self, pos):
        sz = self.get_size()
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < sz[0] and pos[1] < sz[1]
