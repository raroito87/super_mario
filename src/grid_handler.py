from src import Cell, CellType
from src.grid import Grid

import itertools

import math

class GridHandler():

    def __init__(self):
        self.error_flag = False
        self.dict = {'-': CellType.free, 'x': CellType.obstacle, 'm': CellType.mario, 'p': CellType.princess}
        self.dict_directions = {'[-1, 0]': 'UP', '[1, 0]': 'DOWN', '[0, -1]': 'LEFT', '[0, 1]': 'RIGHT'}

    def initialize_grid(self, N, raw_grid):
        if self._is_raw_grid_incorrect(N, raw_grid):
            return

        grid = Grid([[Cell(cell_type=self.dict[list(raw_grid[ix])[iy]], pos=[ix, iy]) for iy in range(N)] for ix in range(N)])

        return grid

    def get_start_end(self, grid):
        start = []
        end = []
        # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        # lat_list = [item for sublist in grid.board for item in sublist]
        flat_list = list(itertools.chain.from_iterable(grid.board))
        for c in flat_list:
            if c.type == CellType.mario:
                start = c.pos
            if c.type == CellType.princess:
                end = c.pos

        return start, end


    def find_shortest_path(self, grid, start, end):
        max_distance = math.inf

        # we start here, thus a distance of 0
        open_list = [start]
        grid.at(start).count = 0

        # (x,y) offsets from current cell
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while open_list:
            # get the next cell pos in the list
            cur_pos = open_list.pop(0)
            cur_cell = grid.at(cur_pos)

            # check the for neighbours in the cell
            for neighbour in neighbours:
                n_cell_pos = self._add_point(cur_pos, neighbour)
                if not grid.is_valid_point(n_cell_pos):
                    continue

                cell = grid.at(n_cell_pos)

                if cell.type == CellType.obstacle:
                    continue

                dist = cur_cell.count + 1
                if dist > max_distance:
                    continue

                # if the neighbor distance is higher than dist
                # means I have now a shorter way
                if cell.count > dist:
                  cell.count = dist
                  cell.path_from = cur_cell
                  cur_cell.path_to = cell
                  open_list.append(n_cell_pos)

        print('finish path search')

        princess_cell = grid.at(end)
        if princess_cell.count == math.inf:
            print('no path found')
            self.error_flag = True
            return

        return self._return_path_to_princess(grid, start, end)

    def _return_path_to_princess(self, grid, start, end):
        """ Returns the path to the end"""
        cell = grid.at(end)
        path = []
        while cell != None:
            path.append(cell.pos)
            cell = cell.path_from

        path_rev = path[::-1]
        dif = []
        for i in range(len(path_rev) - 1):
            dif.append([path_rev[i + 1][0] - path_rev[i][0], path_rev[i + 1][1] - path_rev[i][1]])

        return [self.dict_directions[str(d)] for d in dif]


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

    def _add_point(self, a, b):
        return [a[0] + b[0], a[1] + b[1]]
