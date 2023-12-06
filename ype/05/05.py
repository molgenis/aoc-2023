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
        """Solves the second part of the puzzle.

        The reasoning is as follows:
        the seed that yields the local minimum location number within a seed range is either
        - the lower bound of the seed range
        - mapped to a smaller number as the lower bound in a mapping range.

        Therefore, the number of potentially optimal solutions can be reduced to
        those seeds that at any one stage of the mapping process are the lower bound of a range.
        The minimum solution can then be obtained by comparing the locations
        corresponding to the remaining seeds
        """

        # Construct the ranges of seed numbers from the input
        seed_combos = [self.data['seeds'][2 * i:2 * i + 2] for i in range(int(len(self.data['seeds']) / 2))]
        seed_ranges = [[sc[0], sc[0]+sc[1]] for sc in seed_combos]

        # Create a copy of the mappings indexed with increasing integers instead of mapping names
        mappings = {idx-1: values for idx, (key, values) in enumerate(self.data.items()) if '-' in key}

        # Gather in each mapping the lower bounds of the source ranges
        source_lbs = {
            key: [val[1] for val in values]
            for key, values in mappings.items()
        }

        # Construct the list of seeds that are the lower bound of a range
        lb_seeds = [seed for seed in [sr[0] for sr in seed_ranges]]

        # Iterate over the lower bounds of each mapping and
        # find out to which seed they correspond
        for map_idx, lbs in source_lbs.items():
            for lb in lbs:
                key = map_idx
                source = lb
                while key > min(mappings.keys()):
                    destination = source
                    source = self._find_source(destination, mappings[key-1])
                    key -= 1
                seed = source
                lb_seeds.append(seed)

        # Filter the list of lower bound seeds for those seeds that appear in any of the seed ranges
        lb_seeds = [seed for seed in lb_seeds if any([seed in range(*sr) for sr in seed_ranges])]

        # Find the location numbers for each seed
        seed_to_loc = {}
        for seed in lb_seeds:
            destination = seed
            for key, values in mappings.items():
                source = destination
                destination = self._find_destination(source, values)
            location = destination

            seed_to_loc[seed] = location

        # Find the minimum location number among the results
        min_loc = min(seed_to_loc.values())

        print(f"The minimal location number is {min_loc}.")
        return min_loc

    @staticmethod
    def _find_destination(s: int, _mappings: list[list]) -> int:
        """Finds the destination corresponding to a source number using the mapping."""
        d = s
        for m in _mappings:
            if s in range(m[1], m[1] + m[2]):
                d = m[0] + (s - m[1])
        return d

    @staticmethod
    def _find_source(d: int, _mappings: list[list]) -> int:
        """Find the source corresponding to a destination number using the mapping."""
        s = d
        for m in _mappings:
            if d in range(m[0], m[0] + m[2]):
                s = m[1] + (d - m[0])
        return s

    @staticmethod
    def _read_input(fn: str) -> dict:
        """Reads in the txt file and returns the seed numbers and mappings."""
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
