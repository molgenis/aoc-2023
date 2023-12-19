"""
Script for solving the zeroth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/0
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.rules, self.parts = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        accepted = []
        for part in self.parts:
            if self._is_accepted(part):
                accepted.append(part)

        rating_sum = sum(sum(acc.values()) for acc in accepted)

        print(f"The sum of the ratings equals {rating_sum}.")

        return rating_sum

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        limits = {'x': [], 'm': [], 'a': [], 's': []}
        for rule in self.rules.values():
            for r in rule:
                if '<' in r:
                    cat, lim = r.split(':')[0].split('<')
                    limits[cat].append(int(lim))
                elif '>' in r:
                    cat, lim = r.split(':')[0].split('>')
                    limits[cat].append(int(lim)+1)
                else:
                    pass
        for key, values in limits.items():
            limits[key] = [1] + sorted(limits[key]) + [4001]
        print(limits)
        combinations = 0
        for i_x, x in enumerate(limits['x'][:-1]):
            for i_m, m in enumerate(limits['m'][:-1]):
                for i_a, a in enumerate(limits['a'][:-1]):
                    for i_s, s in enumerate(limits['s'][:-1]):
                        part = {'x': x, 'm': m, 'a': a, 's': s}
                        if self._is_accepted(part):
                            combinations += ((limits['x'][i_x+1] - limits['x'][i_x])
                                             * (limits['m'][i_m+1] - limits['m'][i_m])
                                             * (limits['a'][i_a+1] - limits['a'][i_a])
                                             * (limits['s'][i_s+1] - limits['s'][i_s]))

        print(f"the number of distinct combinations equals {combinations}")

        return combinations

    def _is_accepted(self, part: dict):
        """Verifies whether a part is accepted."""
        rule = 'in'
        while rule not in ['A', 'R']:
            values = self.rules[rule]
            for val in values:
                if ':' not in val:
                    rule = val
                    continue
                if '<' in val:
                    cat, [limit, send_to] = val.split('<')[0], val.split('<')[1].split(':')
                    if part[cat] < int(limit):
                        rule = send_to
                        break
                else:
                    cat, [limit, send_to] = val.split('>')[0], val.split('>')[1].split(':')
                    if part[cat] > int(limit):
                        rule = send_to
                        break

        if rule == 'A':
            return True
        return False

    @staticmethod
    def _read_input(fn: str) -> tuple[dict, list]:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.read().splitlines()

        rules = {}
        idx = 0
        while (line := raw_data[idx]) != '':
            rules.update({line.split('{')[0]: line.split('{')[1].split('}')[0].split(',')})
            idx += 1

        parts = []
        idx += 1
        for idx, line in enumerate(raw_data[idx:]):
            parts.append(dict(zip(
                    map(lambda p: p.split('=')[0], line.split('{')[1].split('}')[0].split(',')),
                    map(lambda p: int(p.split('=')[1]), line.split('{')[1].split('}')[0].split(','))
                )))

        return rules, parts


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '19.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
