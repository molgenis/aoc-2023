"""
Script for solving the twenty-first puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/21
"""

U = (-1, 0)
R = (0, +1)
D = (1, 0)
L = (0, -1)

class Puzzle:
    rocks: list[tuple]
    m: int
    n: int
    S: tuple[int, int]
    num_steps: int

    def __init__(self, filename: str, num_steps: int):
        """Initializes the puzzle."""
        self.rocks, self.S, self.m, self.n = self._load_data(filename)
        self.num_steps = num_steps

    def neighbours(self, i: int, j: int) -> list[tuple[int, int]]:
        """Finds the neighbours of the node."""
        neighbours = []
        for d_i, d_j in [U, R, D, L]:
            if ((i+d_i, j+d_j) not in self.rocks
                    and i+d_i in range(self.m+1)
                    and j+d_j in range(self.n+1)):
                neighbours.append((i+d_i, j+d_j))
        return neighbours


    @staticmethod
    def _load_data(filename: str) -> tuple[list[tuple[int, int]], tuple[int, int], int, int]:
        rocks = []
        with open(filename, 'r') as f:
            for i, row in enumerate(f.readlines()):
                for j, val in enumerate(row):
                    if val == '#':
                        rocks.append((i, j))
                    elif val == 'S':
                        start = (i, j)
        return rocks, start, i, j


class PuzzleSolver:
    """Object to solve a puzzle."""

    def test_part_1(self) -> bool:
        """Tests the first part of the puzzle."""
        assert (result := self.solve_part_1('t1.txt', 6)) == 16, f"Expected 16, got {result}."
        return True


    @staticmethod
    def solve_part_1(filename: str = '21.txt', num_steps: int = 64) -> int:
        """Solves the first part of the puzzle."""
        puzzle = Puzzle(filename, num_steps)

        visited: dict[tuple[int, int], int] = dict()
        unvisited: dict[tuple[int, int], int] = {puzzle.S: 0}

        while min(unvisited.values()) <= num_steps:
            node = min(unvisited, key=unvisited.get)
            steps = unvisited[node]
            neighbours = puzzle.neighbours(*node)
            for nb in neighbours:
                if nb not in [*unvisited.keys(), *visited.keys()]:
                    unvisited[nb] = steps + 1
            if steps % 2 == num_steps % 2:
                visited[node] = unvisited.pop(node)
            else:
                unvisited.pop(node)

        print(f"{len(visited)} garden plots can be reached.")
        return len(visited)

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        


if __name__ == '__main__':
    solver = PuzzleSolver()
    print(f"Testing part 1")
    solver.test_part_1()
    print(f"Solving past 1")
    solver.solve_part_1()
