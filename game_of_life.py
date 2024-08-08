class GameOfLife:
    def __init__(self, rows=100, cols=100, initial_state=None) -> None:
        if max(rows, cols) > 10000:
            raise ValueError("Grid size too large")
        self.game_length = 100
        self.frames = 60
        self.rows = rows
        self.cols = cols
        self.grid = initial_state if initial_state else self.create_empty_grid()

    def create_empty_grid(self) -> list:
        return [[False for _ in range(self.cols)] for _ in range(self.rows)]

    def step(self) -> None:
        new_grid = self.create_empty_grid()

        for i in range(self.rows):
            for j in range(self.cols):
                new_grid[i][j] = self.is_alive(i, j)

        self.grid = new_grid

    def is_alive(self, i, j) -> bool:
        # A live cell dies if it has fewer than two live neighbors.
        # A live cell with two or three live neighbors lives on to the next generation.
        # A live cell with more than three live neighbors dies.
        # A dead cell will be brought back to live if it has exactly three live neighbors.

        # in short
        # if < 2 - dead and > 3 - dead, 2 or 3 - live,
        live_neighbors = self.count_live_neighbors(i, j)
        if self.grid[i][j]:
            return 2 <= live_neighbors <= 3
        else:
            return live_neighbors == 3

    def count_live_neighbors(self, i, j) -> int:
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    count += 1 if self.grid[(i + dx) % self.rows][(j + dy) % self.cols] else 0

        return count

    def toggle_cell(self, row, col) -> None:
        self.grid[row][col] = True