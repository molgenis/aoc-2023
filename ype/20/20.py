"""
Script for solving the twentieth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/20
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self._fn = filename

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        flipflops, cons, destinations = self._read_input(self._fn)

        num_pushes = 1000
        count_low = 0
        count_high = 0


        for _ in range(num_pushes):
            sources: list[tuple[str, int]] = [('broadcaster', 0)]
            count_low += 1
            while len(sources) > 0:
                source, pulse = sources.pop()
                targets = destinations[source]
                for target in targets:
                    if target in flipflops.keys() and pulse == 0:
                        flipflops[target] = 1 - flipflops[target]
                        sources.append((target, flipflops[target]))
                    elif target in cons.keys():
                        cons[target][source] = pulse
                        sources.append((target, 1-(len(cons[target].keys()) == sum(cons[target].values()))))
                    count_low += (pulse == 0)
                    count_high += (pulse == 1)

        print(f"The number of pulses multiplied equals {count_low * count_high}.")
        return count_low * count_high




    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        flipflops, cons, destinations = self._read_input(self._fn)

        final_mod = 'rx'
        pen_mod, = [s for (s, t) in destinations.items() if final_mod in t]
        pen_sources = dict()

        num_pushes = 0

        while len(pen_sources) != len(cons[pen_mod]):
            sources: list[tuple[str, int]] = [('broadcaster', 0)]
            num_pushes += 1
            while len(sources) > 0:
                source, pulse = sources.pop()
                targets = destinations[source]
                for target in targets:
                    if target == pen_mod and pulse == 1 and source not in pen_sources.keys():
                        pen_sources[source] = num_pushes
                    if target in flipflops.keys() and pulse == 0:
                        flipflops[target] = 1 - flipflops[target]
                        sources.append((target, flipflops[target]))
                    elif target in cons.keys():
                        cons[target][source] = pulse
                        sources.append((target,
                                        1-(len(cons[target].keys()) == sum(cons[target].values()))))

        iter_prod = 1
        for ps in pen_sources.values():
            iter_prod *= ps

        print(f"After {iter_prod} pushes the final module is pushed.")
        return iter_prod


    @staticmethod
    def _read_input(fn: str) -> tuple:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.read().splitlines()

        flipflops: dict[str, int] = dict()
        destinations: dict[str, list[str]] = dict()
        conjunctions: dict[str, dict[str, int]] = dict()

        for cable in raw_data:
            if cable.startswith('%'):
                src = cable.split('%')[1].split(' ->')[0]
                destinations.update({src: cable.split('-> ')[1].split(', ')})
                flipflops.update({src: 0})
            elif cable.startswith('&'):
                src = cable.split('&')[1].split(' ->')[0]
                destinations.update({src: cable.split('-> ')[1].split(', ')})
                conjunctions[src] = dict()
            elif cable.startswith('broadcaster'):
                destinations['broadcaster'] = cable.split('-> ')[1].split(', ')

        for src, targets in destinations.items():
            for target in targets:
                if target in conjunctions.keys():
                    conjunctions[target][src] = 0

        return flipflops, conjunctions, destinations


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    # print(f"\nSolution for part 2")
    # test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '20.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
