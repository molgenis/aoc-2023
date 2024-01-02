"""
Script for solving the fourteenth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/14
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data: list = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        total_weigth = 0
        for col in self.data:
            L = len(col)
            r = 0
            ctr = 0
            for idx, ch in enumerate(col):
                if ch == '#':
                    r = idx + 1
                    ctr = 0
                elif ch == 'O':
                    total_weigth += L-(r+ctr)
                    ctr += 1
                else:
                    continue

        print(f"The total weight equals {total_weigth}.")
        return total_weigth

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.read().splitlines()

        row_len = len(raw_data[0])
        columns = [
            [row[idx] for row in raw_data]
            for idx in range(row_len)
        ]

        return columns


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '14.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
