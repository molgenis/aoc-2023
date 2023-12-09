"""
Script for solving the ninth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/9
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.sequences: list = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle.

        The reasoning is as follows:
        for each sequence a sequences of differences of the previous sequence
        are created until the differences all equal zero.
        Then, the last value of all sequences of differences are summed up and
        added to the last value of the original sequence.
        This last summed value is the extrapolated value.
        """
        extrapolated = []
        for seq in self.sequences:
            expol = seq[-1]
            new_seq = seq
            while not all(map(lambda n: n == 0, new_seq)):
                new_seq = list(map(lambda a, b: b - a, new_seq[:-1], new_seq[1:]))
                expol += new_seq[-1]

            extrapolated.append(expol)

        print(f"The sum of the extrapolated values equals {sum(extrapolated)}.")

        return sum(extrapolated)

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle.

        The reasoning is as follows:
        firstly the sequences of differences are generated as in the first part.
        The starting value of each difference sequence are stored in the process.
        The extrapolated value is then the result of subtracting the first value
        of each difference sequence from each other.
        """
        extrapolated = []
        for seq in self.sequences:
            new_seq = seq
            starts = [new_seq[0]]
            while not all(map(lambda n: n == 0, new_seq)):
                new_seq = list(map(lambda a, b: b - a, new_seq[:-1], new_seq[1:]))
                starts.append(new_seq[0])

            expol = sum((-1)**i * val for (i, val) in enumerate(starts))

            extrapolated.append(expol)

        print(f"The sum of the extrapolated values equals {sum(extrapolated)}.")

        return sum(extrapolated)

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        sequences = [
            list(map(int, line.split()))
            for line in raw_data
        ]

        return sequences


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '09.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
