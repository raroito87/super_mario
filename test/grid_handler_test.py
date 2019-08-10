import unittest

from src import GridHandler, Cell, CellType

class GridHandlerTest(unittest.TestCase):

    def test_initialize_grid_proper_size_correct(self):
        N = 3
        list_grid = ['--m','-x-','-p-']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, False)

    def test_initialize_grid_proper_size_incorrect_1(self):
        N = 0
        list_grid = []

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_proper_size_incorrect_2(self):
        N = 0
        list_grid = ['--m','-x-','-p-']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_proper_size_incorrect_3(self):
        N = 3
        list_grid = [123, '-x-', '-p-']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_proper_size_incorrect_4(self):
        N = 3
        list_grid = ['--m-', '-x-', '-p-']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_proper_size_incorrect_5(self):
        N = 3
        list_grid = ['--m-', '-x-', '-p-', '---']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_proper_size_incorrect_6(self):
        N = 3.5
        list_grid = ['--m','-x-','-p-']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_proper_size_incorrect_7(self):
        N = -1
        list_grid = ['--m','-x-','-p-']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_characters_incorrect_1(self):
        N = 3
        list_grid = ['---', '---', '---']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_characters_incorrect_2(self):
        N = 3
        list_grid = ['-m-', '---', '---']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_characters_incorrect_3(self):
        N = 3
        list_grid = ['---', '--p', '---']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_characters_incorrect_4(self):
        N = 3
        list_grid = ['m--', '--p', '--p']

        gr = GridHandler()
        gr.initialize_grid(N, list_grid)
        self.assertEqual(gr.error_flag, True)

    def test_initialize_grid_correct(self):
        N = 3
        list_grid = ['--m', '-x-', '-p-']

        grid_ = [[Cell(cell_type=CellType.free), Cell(cell_type=CellType.free), Cell(cell_type=CellType.mario)],
                 [Cell(cell_type=CellType.free), Cell(cell_type=CellType.obstacle), Cell(cell_type=CellType.free)],
                 [Cell(cell_type=CellType.free), Cell(cell_type=CellType.princess), Cell(cell_type=CellType.free)]]

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)

        self.assertEqual(grid.board[0][0].type == grid_[0][0].type, True)
        self.assertEqual(grid.board[0][1].type == grid_[0][1].type, True)
        self.assertEqual(grid.board[0][2].type == grid_[0][2].type, True)
        self.assertEqual(grid.board[1][0].type == grid_[1][0].type, True)
        self.assertEqual(grid.board[1][1].type == grid_[1][1].type, True)
        self.assertEqual(grid.board[1][2].type == grid_[1][2].type, True)
        self.assertEqual(grid.board[2][0].type == grid_[2][0].type, True)
        self.assertEqual(grid.board[2][1].type == grid_[2][1].type, True)
        self.assertEqual(grid.board[2][2].type == grid_[2][2].type, True)
        self.assertEqual(grid.board[0][0].pos == [0, 0], True)
        self.assertEqual(grid.board[0][1].pos == [0, 1], True)
        self.assertEqual(grid.board[0][2].pos == [0, 2], True)
        self.assertEqual(grid.board[1][0].pos == [1, 0], True)
        self.assertEqual(grid.board[1][1].pos == [1, 1], True)
        self.assertEqual(grid.board[1][2].pos == [1, 2], True)
        self.assertEqual(grid.board[2][0].pos == [2, 0], True)
        self.assertEqual(grid.board[2][1].pos == [2, 1], True)
        self.assertEqual(grid.board[2][2].pos == [2, 2], True)
        self.assertEqual(gr.error_flag, False)

    def test_find_multiple_shortest_path_N3_correct_1(self):
        N = 3
        list_grid = ['--m', '-x-', '-p-']
        paths_true = [['DOWN', 'DOWN', 'LEFT']]

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)
        paths = gr.find_multiple_shortest_paths(grid)

        self.assertEqual(paths == paths_true, True)
        self.assertEqual(gr.error_flag, False)

    def test_find_multiple_shortest_path_N3_correct_2(self):
        N = 3
        list_grid = ['--m', '-x-', '-px']
        paths_true = [['LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT']]

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)
        paths = gr.find_multiple_shortest_paths(grid)

        self.assertEqual(paths == paths_true, True)
        self.assertEqual(gr.error_flag, False)

    def test_find_multiple_shortest_path_N3_incorrect(self):
        N = 3
        list_grid = ['--m', '-x-', 'xpx']

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)
        paths = gr.find_multiple_shortest_paths(grid)

        self.assertEqual(paths is None, True)
        self.assertEqual(gr.error_flag, True)

    def test_find_multiple_shortest_path_N3_multiple_correct_1(self):
        N = 3
        list_grid = ['x-m', '---', '-p-']
        paths_true = [['DOWN', 'DOWN', 'LEFT'], ['DOWN', 'LEFT', 'DOWN'], ['LEFT', 'DOWN', 'DOWN']]

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)
        paths = gr.find_multiple_shortest_paths(grid)

        self.assertEqual(paths == paths_true, True)
        self.assertEqual(gr.error_flag, False)

    def test_find_multiple_shortest_path_N5_multiple_correct_1(self):
        N = 5
        list_grid = ['m----', '-xx--', '-xxxx', '-x---', '---xp']
        paths_true = [['DOWN', 'DOWN', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'RIGHT', 'RIGHT', 'DOWN']]

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)
        paths = gr.find_multiple_shortest_paths(grid)

        self.assertEqual(paths == paths_true, True)
        self.assertEqual(gr.error_flag, False)

    def test_find_multiple_shortest_path_N5_multiple_correct_2(self):
        N = 5
        list_grid = ['p---x', 'xx--x', 'xxx--', '-mx--', '----x']
        paths_true = [['DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'LEFT', 'LEFT'],
                      ['DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'LEFT', 'UP', 'LEFT', 'LEFT']]

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)
        paths = gr.find_multiple_shortest_paths(grid)

        self.assertEqual(paths == paths_true, True)
        self.assertEqual(gr.error_flag, False)

    def test_find_multiple_shortest_path_N5_multiple_correct_3(self):
        N = 4
        list_grid = ['xm--', '-xx-', 'x---', '-px-']
        paths_true = [['RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'DOWN']]

        gr = GridHandler()
        grid = gr.initialize_grid(N, list_grid)
        paths = gr.find_multiple_shortest_paths(grid)

        self.assertEqual(paths == paths_true, True)
        self.assertEqual(gr.error_flag, False)