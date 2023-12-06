"""
Script for solving the second puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/2
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.games: dict = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        possible_games = []
        for idx, sets in self.games.items():
            if all(map(self._is_set_feasible, sets)):
                possible_games.append(idx)

        print(f"The sum of the IDs of the possible games equals {sum(possible_games)}.")

        return sum(possible_games)

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        colors = ['red', 'blue', 'green']
        power_sum = 0
        for idx, sets in self.games.items():
            max_colors = {col: max(_set.get(col, 0) for _set in sets) for col in colors}
            cube_power = 1
            for col_max in max_colors.values():
                cube_power *= col_max
            power_sum += cube_power

        print(f"The sum of the power of the minimum cube sets equals {power_sum}.")

        return power_sum

    @staticmethod
    def _is_set_feasible(_set: dict):
        """Checks if a set of cubes fits the constraint."""
        constraints = {'red': 12, 'green': 13, 'blue': 14}
        return all(v <= constraints[k] for (k, v) in _set.items())

    @staticmethod
    def _read_input(fn: str) -> dict:
        """Reads in the txt file and returns a dictionary of the games."""
        with open(file=fn) as f:
            raw_data = f.readlines()
        games = {
            int(line.split('Game ')[1].split(':')[0]): [
                {cube.split()[1]: int(cube.split()[0]) for cube in _set.split(', ')}
                for _set in line.split(': ')[1].split(';')
            ]
            for line in raw_data
        }

        return games


if __name__ == '__main__':
    print(f"Test solutions.")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions.")
    real_file = '02.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
