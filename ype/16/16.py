"""
Script for solving the sixteenth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/16
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data: list = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        positions = [[0, -1]]
        directions = ['e']

        visited = []

        while len(positions) != 0:
            p = positions.pop(0)
            d = directions.pop(0)
            if [p, d] in visited:
                continue
            if self._is_in_grid(*p) and [p, d] not in visited:
                visited.append([p, d])
            new_p = self._move(p, d)
            if not self._is_in_grid(*new_p):
                continue
            tile_type = self.value(*new_p)
            if tile_type == '.':
                positions.append(new_p)
                directions.append(d)
            elif tile_type == '/':
                new_d = self._next_directions(tile_type, d)
                positions.append(new_p)
                directions.append(new_d)
            elif tile_type == '\\':
                new_d = self._next_directions(tile_type, d)
                positions.append(new_p)
                directions.append(new_d)
            elif tile_type == '|':
                new_ds = self._next_directions(tile_type, d)
                for nd in new_ds:
                    positions.append(new_p)
                    directions.append(nd)
            elif tile_type == '-':
                new_ds = self._next_directions(tile_type, d)
                for nd in new_ds:
                    positions.append(new_p)
                    directions.append(nd)
            else:
                continue
        energized = []
        for v in visited:
            if v[0] not in energized:
                energized.append(v[0])
        print(f"The number of visited tiles equals {len(energized)}.")
        return len(energized)

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        m, n = len(self.data[0]), len(self.data)
        configurations = [
            *[[[i, -1], 'e'] for i in range(m)],
            *[[[-1, j], 's'] for j in range(n)],
            *[[[i, n], 'w'] for i in range(m)],
            *[[[m, j], 'n'] for j in range(n)]
        ]
        max_energized = 0
        for _p, _d in configurations:
            positions = [_p]
            directions = [_d]
            visited = []

            while len(positions) != 0:
                p = positions.pop(0)
                d = directions.pop(0)
                if [p, d] in visited:
                    continue
                if self._is_in_grid(*p) and [p, d] not in visited:
                    visited.append([p, d])
                new_p = self._move(p, d)
                if not self._is_in_grid(*new_p):
                    continue
                tile_type = self.value(*new_p)
                if tile_type == '.':
                    positions.append(new_p)
                    directions.append(d)
                elif tile_type == '/':
                    new_d = self._next_directions(tile_type, d)
                    positions.append(new_p)
                    directions.append(new_d)
                elif tile_type == '\\':
                    new_d = self._next_directions(tile_type, d)
                    positions.append(new_p)
                    directions.append(new_d)
                elif tile_type == '|':
                    new_ds = self._next_directions(tile_type, d)
                    for nd in new_ds:
                        positions.append(new_p)
                        directions.append(nd)
                elif tile_type == '-':
                    new_ds = self._next_directions(tile_type, d)
                    for nd in new_ds:
                        positions.append(new_p)
                        directions.append(nd)
                else:
                    continue
            energized = []
            for v in visited:
                if v[0] not in energized:
                    energized.append(v[0])
            if len(energized) > max_energized:
                max_energized = len(energized)

        print(f"The optimal configuration yields a total number of energized tiles of {max_energized}.")
        return max_energized

    def value(self, r: int, c: int) -> str | None:
        """Returns the type of the tile specified by the row and column indices."""
        try:
            return self.data[r][c]
        except IndexError:
            return None

    def _is_in_grid(self, r: int, c: int) -> bool:
        if min(r, c) < 0:
            return False
        if r+1 > len(self.data):
            return False
        if c+1 > len(self.data[0]):
            return False
        return True

    @staticmethod
    def _move(pos: list[int], di: str) -> list[int]:
        """Moves the position to the new position along the direction."""
        to = {'e': [0, +1], 'n': [-1, 0], 'w': [0, -1], 's': [+1, 0]}
        new_pos = list(map(sum, zip(pos, to[di])))
        return new_pos

    @staticmethod
    def _next_directions(tile: str, d: str) -> str | list:
        """Returns the next directions from the current tile based on
        the direction from which the beam moved into the tile.
        """
        next_directions = {
            '/': {'e': 'n', 'n': 'e', 'w': 's', 's': 'w'},
            '\\': {'e': 's', 's': 'e', 'w': 'n', 'n': 'w'},
            '-': {'e': ['e'], 's': ['e', 'w'], 'w': ['w'], 'n': ['e', 'w']},
            '|': {'e': ['n', 's'], 's': ['s'], 'w': ['n', 's'], 'n': ['n']}
        }

        return next_directions.get(tile).get(d)

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.read().splitlines()

        return raw_data


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '16.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
