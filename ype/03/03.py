"""
Script for solving the third puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/3
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.numbers, self.symbols = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""

    @staticmethod
    def _read_input(fn: str) -> tuple[list, list]:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        numbers = []
        symbols = []
        for i, line in enumerate(raw_data):
            j = 0
            while line[j] != '\n':
                if line[j].isdigit():
                    num = line[j]
                    coords = [i, j]
                    while line[j+1].isdigit():
                        num += line[j+1]
                        j += 1
                    numbers.append([num, coords])
                    j += 1
                elif line[j] in ['.']:
                    j += 1
                    continue
                else:
                    symbols.append([[i, j], line[j]])
                    j += 1

        return numbers, symbols


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '03.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
