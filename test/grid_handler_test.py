import unittest

from src import GridHandler, Cell, CellType

class GridHandlerTest(unittest.TestCase):

    def test_create_grid_proper_size_correct(self):
        N = 3
        list_grid = ['--m','-x-','-p-']

        gr = GridHandler()
        gr.create_grid(N, list_grid)
        self.assertEqual(gr.error_flag, False)

    def test_create_grid_proper_size_incorrect_1(self):
        N = 0
        list_grid = []

        gr = GridHandler()
        gr.create_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_create_grid_proper_size_incorrect_2(self):
        N = 0
        list_grid = ['--m','-x-','-p-']

        gr = GridHandler()
        gr.create_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_create_grid_proper_size_incorrect_3(self):
        # case 3
        N = 3
        list_grid = [123, '-x-', '-p-']

        gr = GridHandler()
        gr.create_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_create_grid_proper_size_incorrect_4(self):
        # case 4
        N = 3
        list_grid = ['--m-', '-x-', '-p-']

        gr = GridHandler()
        gr.create_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_prepare_grid_correct(self):
        N = 3
        list_grid = ['--m', '-x-', '-p-']

        grid_ = [[Cell(cell_type=CellType.free), Cell(cell_type=CellType.free), Cell(cell_type=CellType.mario)],
                 [Cell(cell_type=CellType.free), Cell(cell_type=CellType.obstacle), Cell(cell_type=CellType.free)],
                 [Cell(cell_type=CellType.free), Cell(cell_type=CellType.princess), Cell(cell_type=CellType.free)]]

        gr = GridHandler()
        grid = gr.create_grid(N, list_grid)
        print(grid[0][0].type)
        self.assertEqual(grid[0][0].type == grid_[0][0].type, True)
        self.assertEqual(grid[0][1].type == grid_[0][1].type, True)
        self.assertEqual(grid[0][2].type == grid_[0][2].type, True)
        self.assertEqual(grid[1][0].type == grid_[1][0].type, True)
        self.assertEqual(grid[1][1].type == grid_[1][1].type, True)
        self.assertEqual(grid[1][2].type == grid_[1][2].type, True)
        self.assertEqual(grid[2][0].type == grid_[2][0].type, True)
        self.assertEqual(grid[2][1].type == grid_[2][1].type, True)
        self.assertEqual(grid[2][2].type == grid_[2][2].type, True)
        self.assertEqual(gr.error_flag, False)
