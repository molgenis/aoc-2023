"""
Script for solving the eighth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/8
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.instruction, self.nodes = self._read_input(filename)

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle."""
        steps = 0
        node = 'AAA'
        while node != 'ZZZ':
            instr_idx = steps % len(self.instruction)
            d = self.instruction[instr_idx]
            node = self.nodes[node][d]
            steps += 1

        print(f"The number of steps required equals {steps}.")

        return steps

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""

        a_nodes = [n for n in self.nodes.keys() if n.endswith('A')]
        start_loops = list(map(self._find_loop_length, a_nodes))

        steps = len(self.instruction)
        for loop in start_loops:
            steps *= loop['length']

        print(f"The number of steps required equals {steps}.")

        return steps

    def _find_loop_length(self, node: str):
        """Returns the number of steps at which the 'final' loop
        starts, as well as the length of the final loop.
        """

        loop_starts = {}
        steps = 0
        while node not in loop_starts.keys() or steps == 0:
            loop_starts[node] = int(steps / len(self.instruction))
            for d in self.instruction:
                node = self.nodes[node][d]
                steps += 1

        loop_len = int(steps / len(self.instruction)) - loop_starts[node]
        return {'start': loop_starts[node], 'length': loop_len}


    @staticmethod
    def _read_input(fn: str) -> tuple[str, dict]:
        """Reads in the txt file and returns the parsed data."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        instruction = raw_data[0][:-1]
        nodes = {line.split(' = ')[0]: {'L': line.split('(')[1].split(',')[0],
                                        'R': line.split(', ')[1].split(')')[0]}
                 for line in raw_data[2:]}

        return instruction, nodes


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    test_file = 't2.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '08.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
