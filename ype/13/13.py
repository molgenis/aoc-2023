"""
Script for solving the thirteenth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/13
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.patterns: list = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        note_sum = 0
        for pattern in self.patterns:
            n = len(pattern['h'])

            h_pairs = [j for j in range(n-1) if pattern['h'][j] == pattern['h'][j+1]]
            for p in h_pairs:
                m = min(p, n-p-2)
                if all(map(lambda _m: pattern['h'][p-_m] == pattern['h'][p+_m+1], range(m+1))):
                    note_sum += 100*(p+1)

            n = len(pattern['v'])

            v_pairs = [i for i in range(n-1) if pattern['v'][i] == pattern['v'][i+1]]
            for p in v_pairs:
                m = min(p, n-p-2)
                if all(map(lambda _m: pattern['v'][p-_m] == pattern['v'][p+_m+1], range(m+1))):
                    note_sum += p+1

        print(f"The sum of the not summaries equals {note_sum}.")
        return note_sum

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        note_sum = 0
        for pattern in self.patterns:
            loc_0 = {}
            n = len(pattern['h'])

            h_pairs = [j for j in range(n-1) if pattern['h'][j] == pattern['h'][j+1]]
            for p in h_pairs:
                m = min(p, n-p-2)
                if all(map(lambda _m: pattern['h'][p-_m] == pattern['h'][p+_m+1], range(m+1))):
                    loc_0 = {'h': p}

            n = len(pattern['v'])

            v_pairs = [i for i in range(n-1) if pattern['v'][i] == pattern['v'][i+1]]
            for p in v_pairs:
                m = min(p, n-p-2)
                if all(map(lambda _m: pattern['v'][p-_m] == pattern['v'][p+_m+1], range(m+1))):
                    loc_0 = {'v': p}

            for row in range(len(pattern['h'])):
                for col in range(len(pattern['h'][row])):
                    _pattern = pattern.copy()
                    # _pattern['h'][row][col] = '.' if pattern['h'][row][col] == '#' else '#'
                    _pattern['h'][row] = str(pattern['h'][row][:col]) \
                                         + ('.' if pattern['h'][row][col] == '#' else '#') \
                                         + str(pattern['h'][row][min(col+1, len(pattern['h'])):])

                    n = len(pattern['h'])
                    h_pairs = [j for j in range(n-1) if _pattern['h'][j] == _pattern['h'][j+1]]
                    for p in h_pairs:
                        m = min(p, n-p-2)
                        if all(map(lambda _m: _pattern['h'][p-_m] == _pattern['h'][p+_m+1], range(m+1))):
                            if {'h': p} != loc_0:
                                note_sum += 100*(p+1)

                    # _pattern['v'][col][row] = '.' if pattern['v'][col][row] == '#' else '#'
                    _pattern['v'][col] = str(pattern['v'][col][:row]) \
                                         + ('.' if pattern['v'][col][row] == '#' else '#') \
                                         + str(pattern['v'][col][min(row+1, len(pattern['v'])):])

                    n = len(pattern['v'])

                    v_pairs = [i for i in range(n-1) if _pattern['v'][i] == _pattern['v'][i+1]]
                    for p in v_pairs:
                        m = min(p, n-p-2)
                        if all(map(lambda _m: _pattern['v'][p-_m] == _pattern['v'][p+_m+1], range(m+1))):
                            if {'v': p} != loc_0:
                                note_sum += p+1

        print(f"The sum of the not summaries equals {note_sum}.")
        return note_sum

    @staticmethod
    def _read_input(fn: str) -> list:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.read().splitlines()
        raw_patterns = []
        pattern = []
        for line in raw_data:
            if line != '':
                pattern.append(line)
            else:
                raw_patterns.append(pattern)
                pattern = []
        raw_patterns.append(pattern)

        patterns = [
            {'h': p,
             'v': list(map(lambda j: ''.join(p[i][j] for i in range(len(p))), range(len(p[0]))))}
            for p in raw_patterns
        ]

        return patterns


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '13.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
