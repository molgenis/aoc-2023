"""
Script for solving the seventeenth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/17
"""

N = 1
E = 2
S = 3
W = 4

class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data: list = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        m = len(self.data)
        n = len(self.data[0])
        visited = dict()
        unvisited = {(0, 0, 2, 0): 0}

        while len(unvisited) != 0:
            # Initialize the list of neighbours
            neighbours = []
            # Get unvisited with minimum distance
            i, j, d, v = min(unvisited, key=unvisited.get)
            heat = unvisited.get((i, j, d, v))
            # Find suitable neighbours
            if d == N:
                neighbours.append((i-1, j, N, v+1))
                neighbours.append((i, j+1, E, 1))
                neighbours.append((i, j-1, W, 1))
            elif d == E:
                neighbours.append((i, j+1, E, v+1))
                neighbours.append((i+1, j, S, 1))
                neighbours.append((i-1, j, N, 1))
            elif d == S:
                neighbours.append((i+1, j, S, v+1))
                neighbours.append((i, j+1, E, 1))
                neighbours.append((i, j-1, W, 1))
            elif d == W:
                neighbours.append((i-1, j, N, 1))
                neighbours.append((i+1, j, S, 1))
                neighbours.append((i, j-1, W, v+1))

            # Append current node to visited
            visited[(i, j, d, v)] = heat
            if len(visited.keys()) % 1000 == 0:
                print(f"Visited {len(visited.keys())} nodes.")
            # Remove current node from unvisited
            unvisited.pop((i, j, d, v))

            # Update unvisited with neighbours
            for _i, _j, _d, _v in neighbours:
                if (_i, _j, _d, _v) in unvisited:
                    if unvisited.get((_i, _j, _d, _v)) > heat + self.data[_i][_j]:
                        unvisited[(_i, _j, _d, _v)] = heat + self.data[_i][_j]
                elif (_i, _j, _d, _v) not in visited:
                    if _i + _j == 0:
                        continue
                    if _v > 3:
                        continue
                    if _i < 0 or _j < 0 or _i > m-1 or _j > n-1:
                        continue
                    unvisited[(_i, _j, _d, _v)] = heat + self.data[_i][_j]

        destinations = [(i, j, d, v) for (i, j, d, v) in visited if i == m-1 and j == n-1]
        dest_dists = {k: v for (k, v) in visited.items() if k in destinations}
        min_dest_dist = min(dest_dists.values())

        print(f"The least heat loss that can be incurred equals {min_dest_dist}.")
        return min_dest_dist

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        m = len(self.data)
        n = len(self.data[0])
        visited = dict()
        unvisited = {(0, 0, 2, 0): 0, (0, 0, 3, 0): 0}

        while len(unvisited.keys()) != 0:
            # Initialize the list of neighbours
            neighbours = []
            # Get unvisited with minimum distance
            i, j, d, v = min(unvisited, key=unvisited.get)
            heat = unvisited.get((i, j, d, v))
            # Find suitable neighbours
            if d == N:
                if v < 10:
                    neighbours.append((i-1, j, N, v+1))
                if v >= 4:
                    neighbours.append((i, j+1, E, 1))
                    neighbours.append((i, j-1, W, 1))
            elif d == E:
                if v < 10:
                    neighbours.append((i, j+1, E, v+1))
                if v >= 4:
                    neighbours.append((i+1, j, S, 1))
                    neighbours.append((i-1, j, N, 1))
            elif d == S:
                if v < 10:
                    neighbours.append((i+1, j, S, v+1))
                if v >= 4:
                    neighbours.append((i, j+1, E, 1))
                    neighbours.append((i, j-1, W, 1))
            elif d == W:
                if v < 10:
                    neighbours.append((i, j-1, W, v+1))
                if v >= 4:
                    neighbours.append((i-1, j, N, 1))
                    neighbours.append((i+1, j, S, 1))

            # Append current node to visited
            visited[(i, j, d, v)] = heat
            if len(visited.keys()) % 1000 == 0:
                print(f"Visited {len(visited.keys())} nodes.")
            # Remove current node from unvisited
            unvisited.pop((i, j, d, v))

            # Update unvisited with neighbours
            for _i, _j, _d, _v in neighbours:
                if (_i, _j, _d, _v) in unvisited:
                    if unvisited.get((_i, _j, _d, _v)) > heat + self.data[_i][_j]:
                        unvisited[(_i, _j, _d, _v)] = heat + self.data[_i][_j]
                elif (_i, _j, _d, _v) not in visited:
                    if _i + _j == 0:
                        continue
                    if _i < 0 or _j < 0 or _i > m-1 or _j > n-1:
                        continue
                    unvisited[(_i, _j, _d, _v)] = heat + self.data[_i][_j]

        destinations = [(i, j, d, v) for (i, j, d, v) in visited if i == m-1 and j == n-1 and v >= 4]
        dest_dists = {k: v for (k, v) in visited.items() if k in destinations}
        min_dest_dist = min(dest_dists.values())

        print(f"The least heat loss that can be incurred using the ultra crucible equals {min_dest_dist}.")
        return min_dest_dist

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.readlines()
        data = [list(map(int, list(row.split('\n')[0]))) for row in raw_data]

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
    real_file = '17.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
