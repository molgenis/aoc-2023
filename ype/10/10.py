"""
Script for solving the tenth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/10
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.tiles: list = self._read_input(filename)
        self.pipes = {
            '|': [[0, +1], [0, -1]],
            '-': [[+1, 0], [-1, 0]],
            'L': [[0, -1], [+1, 0]],
            'J': [[0, -1], [-1, 0]],
            '7': [[0, +1], [-1, 0]],
            'F': [[0, +1], [+1, 0]],
            '.': [[0, 0], [0, 0]],
            'S': [[+100, +100], [+100, +100]]
        }

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle.

        The idea is to 'walk' in both directions from the starting tile until both
        itineraries meet at the same tile.
        This tile must then be the one farthest from the starting tile.
        """

        # Find the starting tile and the tiles connected to the starting tile
        s_tile, = [[i, j] for j in range(len(self.tiles[0])) for (i, row) in enumerate(self.tiles) if row[j] == 'S']
        current_tiles = [
            [s_tile, [i, j]]
            for j in range(len(self.tiles[0])) for (i, row) in enumerate(self.tiles)
            if any(map(lambda p: [i+p[1], j+p[0]] == s_tile, self.pipes[self.tiles[i][j]]))
        ]

        # In each iteration, find for both itinerary the tile that is connected
        # to the current tile that is unequal to the previous tile
        steps = 1
        while current_tiles[0][1] != current_tiles[1][1]:
            next_tiles = []
            for ct in current_tiles:
                for p in self.pipes[self.tiles[ct[1][0]][ct[1][1]]]:
                    if (nt := [ct[1][0] + p[1], ct[1][1] + p[0]]) != ct[0]:
                        next_tiles.append(nt)
            current_tiles = list(map(lambda _ct, _nt: [_ct[1], _nt], current_tiles, next_tiles))
            steps += 1

        print(f"The number of steps to the farthest position equals {steps}.")

        return steps

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.readlines()
        tiles = [list(row.strip()) for row in raw_data]

        return tiles


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '10.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
