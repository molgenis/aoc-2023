"""
Script for solving the fifteenth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/15
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data: list = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        results = 0
        for s in self.data:
            r = 0
            for ch in s:
                r += ord(ch)
                r *= 17
                r %= 256
            results += r

        print(f"The total sum of the results equals {results}.")
        return results

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        boxes: list[dict] = [{} for _ in range(256)]
        for seq in self.data:
            if '-' in seq:
                label = seq.split('-')[0]
                box = 0
                for ch in label:
                    box += ord(ch)
                    box *= 17
                    box %= 256
                if label in boxes[box].keys():
                    boxes[box].pop(label)

            if '=' in seq:
                label, strength = seq.split('=')
                box = 0
                for ch in label:
                    box += ord(ch)
                    box *= 17
                    box %= 256
                boxes[box].update({label: int(strength)})

        focus_power = 0
        for i, b in enumerate(boxes):
            for j, bv in enumerate(b.values()):
                focus_power += (i+1)*(j+1)*bv

        print(f"The total focus power equals {focus_power}.")
        return focus_power

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.read().splitlines()
        sequence = raw_data[0].split(',')

        return sequence


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '15.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
