"""
Script for solving the third puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/3
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.numbers, self.symbols = self._read_input(filename)

    def __str__(self):
        return "Solver for the puzzle 3"

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        part_sum = 0
        sym_locs = list(map(lambda sym: sym[1], self.symbols))
        for num in self.numbers:
            n_len = len(num[0])
            row_range = range(max(0, num[1][0]-1), num[1][0]+2)
            col_range = range(max(0, num[1][1]-1), num[1][1]+n_len+1)
            if any([i, j] in sym_locs for j in col_range for i in row_range):
                part_sum += int(num[0])

        print(f"The total part sum equals {part_sum}.")
        return part_sum

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        gear_ratio_sum = 0
        gears = [sym[1] for sym in self.symbols if sym[0] == '*']
        range_boxes = [
            [num[0],
             [range(max(0, num[1][0]-1), num[1][0]+2),
              range(max(0, num[1][1]-1), num[1][1]+len(num[0])+1)]]
            for num in self.numbers
        ]
        gear_numbers = [
            [num[0] for num in range_boxes
             if any(gear == [i, j] for i in num[1][0] for j in num[1][1])]
            for gear in gears
        ]
        for gn in gear_numbers:
            if len(gn) == 2:
                gear_ratio_sum += int(gn[0]) * int(gn[1])

        print(f"The sum of all gear ratios equals {gear_ratio_sum}.")

        return gear_ratio_sum

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
                    coord = [i, j]
                    num = line[j]
                    while line[j+1].isdigit():
                        num += line[j+1]
                        j += 1
                    numbers.append([num, coord])
                    j += 1
                elif line[j] == '.':
                    j += 1
                else:
                    coord = [i, j]
                    symbols.append([line[j], coord])
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
