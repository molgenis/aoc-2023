"""
Script for solving the fifth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/5
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data: dict = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        loc_nums = []

        for seed in self.data['seeds']:
            destination = seed
            for key, values in self.data.items():
                if '-' not in key:
                    continue
                source = destination
                destination = self._find_destination(source, values)

            loc_nums.append(destination)

        print(f"The minimal location number is {min(loc_nums)}.")
        return min(loc_nums)

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""

    @staticmethod
    def _find_destination(_s: int, _mappings: list[list]) -> int:
        """Finds the destination corresponding to a source number using the mapping."""
        _d = _s
        for _m in _mappings:
            if _s in range(_m[1], _m[1] + _m[2]):
                _d = _m[0] + (_s - _m[1])
        return _d

    @staticmethod
    def _read_input(fn: str) -> dict:
        """Reads in the txt file and returns the list of cards."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        data = {}
        current_map = ''
        for line in raw_data:
            if line.startswith('seeds'):
                data['seeds'] = list(map(int, line.split('seeds:')[1].split()))
            elif ' map' in line:
                current_map = line.split(' map')[0]
                data[current_map]: list[list] = []
            elif line == '\n':
                continue
            else:
                data[current_map].append(list(map(int, line.split())))

        return data


if __name__ == '__main__':
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    test_solution_1 = test_solver.solve_part_1()
    test_solution_2 = test_solver.solve_part_2()

    real_file = '05.txt'
    real_solver = PuzzleSolver(real_file)
    real_solution_1 = real_solver.solve_part_1()
    real_solution_2 = real_solver.solve_part_2()
