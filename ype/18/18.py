"""
Script for solving the eighteenth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/18
"""

U = 1
D = 2
L = 3
R = 4

class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.dig_plan: list = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        # Establish the boundaries of the grid
        i_min, i_max = 0, 0
        j_min, j_max = 0, 0
        i, j = 0, 0
        for d, v, col in self.dig_plan:
            if d == U:
                i -= v
                i_min = min(i, i_min)
            elif d == R:
                j += v
                j_max = max(j, j_max)
            elif d == D:
                i += v
                i_max = max(i, i_max)
            elif d == L:
                j -= v
                j_min = min(j, j_min)
        m = i_max - i_min + 1
        n = j_max - j_min + 1

        edges = [['O' for j in range(n)] for i in range(m)]

        # Color the trenches in the terrain
        (i, j) = (-i_min, -j_min)
        last_dir = U
        for d, v, _ in self.dig_plan:
            edges[i][j] = '\\' * ((d + last_dir) % 2 == 0) + '/' * ((d + last_dir) % 2 == 1)
            if d == U:
                for _v in range(1, v+1):
                    edges[i-_v][j] = '|'
                i -= v
            elif d == R:
                for _v in range(1, v+1):
                    edges[i][j+_v] = '-'
                j += v
            elif d == D:
                for _v in range(1, v+1):
                    edges[i+_v][j] = '|'
                i += v
            elif d == L:
                for _v in range(1, v+1):
                    edges[i][j-_v] = '-'
                j -= v
            last_dir = d
        edges[i][j] = ('\\' * ((d + self.dig_plan[0][0]) % 2 == 0)
                       + '/' * ((d + self.dig_plan[0][0]) % 2 == 1))

        terrain = [''.join(row) for row in edges]
        # Dig the inside
        lava_limit = 0
        for i in range(m):
            for j in range(n):
                if edges[i][j] == 'O':
                    if sum(map(lambda ch: terrain[i][j:].replace('-', '').count(ch),
                               ['//', '\\\\', '|'])) % 2 > 0:
                        terrain[i] = terrain[i][:j] + 'X' + terrain[i][j+1:]
                        lava_limit += 1
                else:
                    lava_limit += 1

        # Compute the size of the pool
        # lava_limit = sum(sum(row) for row in terrain)

        print(f"The lagoon can hold {lava_limit} cubic meters of lava.")

        return lava_limit



    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        data = []
        dir_map = {'U': 1, 'D': 2, 'L': 3, 'R': 4}
        with open(file=fn) as f:
            for line in f:
                line_data = line.split('\n')[0].split(' ')
                data.append((dir_map.get(line_data[0]), int(line_data[1]), line_data[2]))

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
    real_file = '18.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
