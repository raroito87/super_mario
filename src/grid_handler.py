from src import Cell, CellType
from src.grid import Grid

import itertools

import math
import copy

class GridHandler():

    def __init__(self):
        self.error_flag = False
        self.dict = {'-': CellType.free, 'x': CellType.obstacle, 'm': CellType.mario, 'p': CellType.princess}
        self.dict_directions = {'[-1, 0]': 'UP', '[1, 0]': 'DOWN', '[0, -1]': 'LEFT', '[0, 1]': 'RIGHT'}
        self.all_paths = []

    def initialize_grid(self, N, raw_grid):
        if self._is_raw_grid_incorrect(N, raw_grid):
            print('raw grid is incorrect')
            return None

        return Grid([[Cell(cell_type=self.dict[list(raw_grid[ix])[iy]], pos=[ix, iy]) for iy in range(N)] for ix in range(N)])

    def find_multiple_shortest_paths(self, grid):
        if grid is None:
            self.error_flag = True
            return None

        start, end = self._get_start_end(grid)
        if start is None or end is None:
            self.error_flag = True
            return None

        grid = self._fill_grid_distances(grid, start, end)
        return self._return_all_paths_to_princess(grid, end)

    def _get_start_end(self, grid):
        if grid is None:
            self.error_flag = True
            return None, None

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

    def _fill_grid_distances(self, grid, start, end):
        if grid is None or start is None or end is None:
            self.error_flag = True
            return None

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
                    cell.paths_from.clear()
                    cell.count = dist
                    cell.path_from = cur_cell
                    cell.paths_from.append(cur_cell)
                    open_list.append(n_cell_pos)
                elif cell.count == dist:# same distance I add another parent
                    cell.paths_from.append(cur_cell)

        princess_cell = grid.at(end)
        if princess_cell.count == math.inf:
            print('no path found')
            self.error_flag = True
            return None

        return grid

    def _return_all_paths_to_princess(self, grid, end):
        if grid is None or end is None:
            self.error_flag = True
            return None

        # Returns all shortest paths to the end
        cell = grid.at(end)
        path = []
        self.all_paths.clear()

        self._recurrent(cell, path)
        return [self._path_to_move_str(path) for path in self.all_paths]

    def _recurrent(self, cell, path):
        if cell.type == CellType.mario:
            # save path
            path.append(cell.pos)
            self.all_paths.append(path)
            return

        path.append(cell.pos)
        for p_c in cell.paths_from:
            self._recurrent(p_c, copy.deepcopy(path))

    def _path_to_move_str(self, path):
        path_rev = path[::-1]
        dif = []
        for i in range(len(path_rev) - 1):
            dif.append([path_rev[i + 1][0] - path_rev[i][0], path_rev[i + 1][1] - path_rev[i][1]])

        return [self.dict_directions[str(d)] for d in dif]

    def _is_raw_grid_incorrect(self, N, raw_grid):
        if not isinstance(N, int) or N < 1 or N is not len(raw_grid):
            self.error_flag = True
            return True

        n_m = 0
        n_p = 0
        for s in raw_grid:
            if isinstance(s, str) and len(s) == N:
                n_m += s.count('m')
                n_p += s.count('p')
                continue
            else:
                self.error_flag = True
                return True

        if n_m is not 1 or n_p is not 1:
            self.error_flag = True
            return True

        return False

    def _add_point(self, a, b):
        return [a[0] + b[0], a[1] + b[1]]
