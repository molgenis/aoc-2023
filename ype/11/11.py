"""
Script for solving the eleventh puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/11
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.galaxies, self.ngr, self.ngc = self._read_input(filename)

    def __str__(self):
        return "Solver for puzzle 11"

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle.

        The reasoning is as follows:
        after identifying the locations of the galaxies and the rows and columns without a galaxy,
        the locations of the galaxies are 'moved' by the number of empty rows and columns that precede them.
        Then the distances between each galaxy are calculated by summing the distances column-wise and row-wise.
        The actual length between the galaxies is then half of the sum of distances calculated in the previous step.
        """

        # Expand the universe
        galaxies = [
            [i + sum(map(lambda ngc: ngc < i, self.ngc)),
             j + sum(map(lambda ngr: ngr < j, self.ngr))]
            for i, j in self.galaxies
        ]

        # Tally the distances between each galaxy
        length_sum = sum(max(a[0]-b[0], b[0]-a[0]) + max(a[1]-b[1], b[1]-a[1])
                         for a in galaxies for b in galaxies)

        # Halve the sum
        length_sum = int(length_sum/2)

        print(f"The sum of the lengths equals {length_sum}.")
        return length_sum

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle.

        The solution for this part follows the same reasoning and procedures as in part one
        with the exception that the empty rows and columns in the original universe are
        replaced with 1000000 empty rows and columns.
        """

        # Expand the universe
        factor = 1_000_000 - 1
        galaxies = [
            [i + factor * sum(map(lambda ngc: ngc < i, self.ngc)),
             j + factor * sum(map(lambda ngr: ngr < j, self.ngr))]
            for i, j in self.galaxies
        ]

        # Tally the distances between each galaxy
        length_sum = sum(max(a[0]-b[0], b[0]-a[0]) + max(a[1]-b[1], b[1]-a[1])
                         for a in galaxies for b in galaxies)

        # Halve the sum
        length_sum = int(length_sum/2)
        print(f"The sum of the lengths equals {length_sum}.")
        return length_sum

    @staticmethod
    def _read_input(fn: str) -> tuple[list, list, list]:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.read().splitlines()

        galaxies = [[i, j] for (j, row) in enumerate(raw_data) for i in range(len(row)) if row[i] == '#']
        no_gal_rows = [j for (j, row) in enumerate(raw_data) if '#' not in row]
        no_gal_cols = [i for i in range(len(raw_data[0])) if all(map(lambda row: row[i] == '.', raw_data))]

        return galaxies, no_gal_rows, no_gal_cols


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '11.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
