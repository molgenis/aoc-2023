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
        combinations = 0
        ranges = [{
            'x': range(1, 4001),
            'm': range(1, 4001),
            'a': range(1, 4001),
            's': range(1, 4001)
        }]
        send_to = ['in']

        while len(ranges) != 0:
            r = ranges.pop(0)
            s = send_to.pop(0)
            for rule in self.rules[s]:
                if ':' not in rule:
                    if rule == 'R':
                        continue
                    elif rule == 'A':
                        combinations += self._range_product(r)
                    else:
                        ranges.append(r)
                        send_to.append(rule)
                elif '<' in rule:
                    cat, [limit, _send_to] = rule.split('<')[0], rule.split('<')[1].split(':')
                    _r = {
                        k: (v if k != cat else range(v.start, int(limit)))
                        for k, v in r.items()
                    }
                    r = {
                        k: (v if k != cat else range(int(limit), v.stop))
                        for k, v in r.items()
                    }
                    if _send_to == 'R':
                        pass
                    elif _send_to == 'A':
                        combinations += self._range_product(_r)
                    else:
                        ranges.append(_r)
                        send_to.append(_send_to)
                else:
                    cat, [limit, _send_to] = rule.split('>')[0], rule.split('>')[1].split(':')
                    _r = {
                        k: (v if k != cat else range(int(limit)+1, v.stop))
                        for k, v in r.items()
                    }
                    r = {
                        k: (v if k != cat else range(v.start, int(limit)+1))
                        for k, v in r.items()
                    }
                    if _send_to == 'R':
                        pass
                    elif _send_to == 'A':
                        combinations += self._range_product(_r)
                    else:
                        ranges.append(_r)
                        send_to.append(_send_to)

        print(f"the number of distinct combinations equals {combinations}")

        return combinations

    @staticmethod
    def _range_product(_r: dict) -> int:
        """Calculates the number of combinations of the ranges."""
        prod = 1
        for v in _r.values():
            prod *= len(v)
        return prod

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

    def _prepare_rules(self) -> dict:
        """Modifies the set of rules to reduce the number of rules required to be checked."""
        _rules = self.rules.copy()
        changes = 100
        while changes != 0:
            changes = 0
            for key, values in _rules.items():
                if len(values) > 1 and all(map(lambda r: r.split(':')[-1] == 'A', values[-2:])):
                    _rules[key] = values[:-2] + ['A']
                    changes += 1
                elif len(values) > 1 and all(map(lambda r: r.split(':')[-1] == 'R', values[-2:])):
                    _rules[key] = values[:-2] + ['R']
                    changes += 1
                elif len(values) == 1 and values[0] == 'A':
                    _rules = {
                        _k: [_r.replace(key, 'A') for _r in _v]
                        for _k, _v in _rules.items() if _v[0] != 'A'
                    }
                    changes += 1
                elif len(values) == 1 and values[0] == 'R':
                    _rules = {
                        _k: [_r.replace(key, 'R') for _r in _v]
                        for _k, _v in _rules.items() if _v[0] != 'R'
                    }
                    changes += 1

        return _rules

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
