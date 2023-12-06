"""
Script for solving the first puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/1
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        calibration_values = []
        for line in self.data:
            digits = [ch for ch in line if ch.isdigit()]
            cal_val = int(digits[0] + digits[-1])
            calibration_values.append(cal_val)
        print(f"Sum of all calibration values: {sum(calibration_values)}")

        return sum(calibration_values)

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        calibration_values = []
        for line in self.data:
            digits = []
            for i, ch in enumerate(line):
                if ch.isdigit():
                    digits.append(ch)
                elif any(map(line[i:].startswith, nums.keys())):
                    digits.extend(str(nums[n]) for n in nums.keys() if line[i:].startswith(n))

            cal_val = int(digits[0] + digits[-1])
            calibration_values.append(cal_val)
        print(f"Sum of all calibration values: {sum(calibration_values)}")

        return sum(calibration_values)

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the lines of text."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        return raw_data


if __name__ == '__main__':
    print(f"Test solutions")
    test1_file = 't1.txt'
    test1_solver = PuzzleSolver(test1_file)
    print(f"\nSolution for part 1")
    test1_solution_1 = test1_solver.solve_part_1()
    test2_file = 't2.txt'
    test2_solver = PuzzleSolver(test2_file)
    print(f"\nSolution for part 2")
    test_solution_2 = test2_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '01.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
