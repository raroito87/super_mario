import unittest
from src import MarioAndPrincess

class MarioAndPrincessTest(unittest.TestCase):

    def test_mario_and_princess_correct(self):
        N = 3
        list_grid = ['--m', '-x-', '-px']
        paths_true = [['LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT']]

        paths, error_flag = MarioAndPrincess().get_paths(N, list_grid)

        self.assertEqual(paths == paths_true, True)
        self.assertEqual(error_flag, False)

    def test_mario_and_princess_incorrect(self):
        N = 3
        list_grid = ['--m', '-x-', '-xx']

        paths, error_flag = MarioAndPrincess().get_paths(N, list_grid)

        self.assertEqual(paths is None, True)
        self.assertEqual(error_flag, True)

