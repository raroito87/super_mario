import enum
import math

class CellType(enum.Enum):
    free = 0
    obstacle = 1
    mario = 2
    princess = 3

class Cell():
    def __init__(self, cell_type=CellType.free, pos=None):
        self.type = cell_type
        self.count = math.inf
        self.paths_from = []
        self.pos = pos




