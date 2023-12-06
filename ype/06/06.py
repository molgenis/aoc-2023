"""
Script for solving the sixth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/6
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data_1: dict = self._read_input(filename, q=1)
        self.data_2: dict = self._read_input(filename, q=2)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        solution_product = 1
        for T, D in self.data_1.items():
            ms = 0
            while ms * (T - ms) <= D:
                ms += 1
            solution_range = T + 1 - 2*ms
            solution_product *= solution_range

        print(f"The product of the solutions equals {solution_product}")

        return solution_product

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        T, D = list(self.data_2.items())[0]
        ms = 0
        while ms * (T - ms) <= D:
            ms += 1
        solution_range = T + 1 - 2*ms

        print(f"The length of the range of solutions equals {solution_range}")

        return solution_range

    @staticmethod
    def _read_input(fn: str, q: int) -> dict:
        """Reads in the txt file and returns a dictionary of time and distance."""
        with open(file=fn) as f:
            raw_data = f.readlines()
        if q == 1:
            data = {int(T): int(D) for (T, D) in zip(raw_data[0].split('Time:')[1].split(),
                                                     raw_data[1].split('Distance:')[1].split())}
        elif q == 2:
            data = {int(''.join(raw_data[0].split('Time:')[1].split())):
                    int(''.join(raw_data[1].split('Distance:')[1].split()))}
        else:
            data = {}
        return data


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '06.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
