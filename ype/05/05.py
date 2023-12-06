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

        # Find for each seed the location by trickling them through the mappings
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

        # Construct the ranges of seed numbers from the input
        seed_combos = [self.data['seeds'][2 * i:2 * i + 2] for i in range(int(len(self.data['seeds']) / 2))]
        seed_ranges = [[sc[0], sc[0]+sc[1]] for sc in seed_combos]

        # Create a copy of the mappings indexed with increasing integers instead of mapping names
        mappings = {idx-1: values for idx, (key, values) in enumerate(self.data.items()) if '-' in key}

        # Gather in each mapping the lower bounds of the ranges
        source_lbs = {
            key: [val[1] for val in values]
            for key, values in mappings.items()
        }

        # Iterate over the lower bounds of each mapping and
        # find out to which seed and location number they correspond
        seed_to_loc = {}
        for map_idx, lbs in source_lbs.items():
            for lb in lbs:
                _key = map_idx
                d = lb
                while _key <= max(mappings.keys()):
                    s = d
                    d = self._find_destination(s, mappings[_key])
                    _key += 1
                loc = d

                _key = map_idx
                s = lb
                while _key > min(mappings.keys()):
                    d = s
                    s = self._find_source(d, mappings[_key-1])
                    _key -= 1
                seed = s
                seed_to_loc.update({seed: loc})

        # Filter the seed-to-location dictionary for those seeds that appear in any of the seed ranges
        seed_to_loc = {
            seed: loc
            for seed, loc in seed_to_loc.copy().items()
            if any([seed in range(*sr) for sr in seed_ranges])
        }

        # Find the minimum location number among the valid combinations
        min_loc = min(seed_to_loc.values())

        print(f"The minimal location number is {min_loc}.")
        return min_loc

    @staticmethod
    def _find_destination(_s: int, _mappings: list[list]) -> int:
        """Finds the destination corresponding to a source number using the mapping."""
        _d = _s
        for _m in _mappings:
            if _s in range(_m[1], _m[1] + _m[2]):
                _d = _m[0] + (_s - _m[1])
                break
        return _d

    @staticmethod
    def _find_source(_d: int, _mappings: list[list]) -> int:
        """Find the source corresponding to a destination number using the mapping."""
        _s = _d
        for _m in _mappings:
            if _d in range(_m[0], _m[0] + _m[2]):
                _s = _m[1] + (_d - _m[0])
                break
        return _s

    def _seed_range(self):
        """Returns a seed from one of the ranges without storing all possible seeds in memory."""
        seed_combos = [self.data['seeds'][2*i:2*i+2] for i in range(int(len(self.data['seeds'])/2))]
        for sc in seed_combos:
            for _seed in range(sc[0], sc[0]+sc[1]):
                yield _seed

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
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '05.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
