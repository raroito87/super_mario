from src.grid_handler import GridHandler

class MarioAndPrincess():

    def __init__(self):
        self.handler = GridHandler()

    def get_paths(self, N, raw_grid):

        return self.handler.find_multiple_shortest_paths(self.handler.initialize_grid(N, raw_grid)), self.handler.error_flag

