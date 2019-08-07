from src import Cell, CellType

class GridHandler():

    def __init__(self):
        self.error_flag = False
        self.dict = {'-': CellType.free, 'x':CellType.obstacle, 'm':CellType.mario, 'p':CellType.princess}

    def create_grid(self, N, raw_grid):
        if self._is_raw_grid_incorrect(N, raw_grid):
            return
        grid = []
        for s in raw_grid:
            grid.append([Cell(cell_type=self.dict[c]) for c in list(s)])

        return grid



    def _is_raw_grid_incorrect(self, N, raw_grid):
        if N < 1 or N is not len(raw_grid):
            self.error_flag = True
            return True

        for s in raw_grid:
            if isinstance(s, str) and len(s) == 3:
                continue
            else:
                self.error_flag = True
                return True

        return False