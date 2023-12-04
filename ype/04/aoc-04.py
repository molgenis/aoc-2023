"""
Script to solve the fourth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/4
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data = self._read_input(filename)

    def solve(self, show_matching: bool = False) -> int:
        """Solves the puzzle based on input."""
        if show_matching:
            print("Matching numbers:")
        scores = {}
        for card, numbers in self.data.items():
            winning_nums = list(set(numbers['win_nums']) & set(numbers['my_nums']))
            if (n := len(winning_nums)) == 0:
                scores.update({card: 0})
            else:
                scores.update({card: 2**(n-1)})
            if show_matching:
                print(f"{card:3}: {winning_nums}")

        print("The scores of each card equals: ")
        for card, score in scores.items():
            print(f"{card:3}: {score}")

        print(f"The total score equals: {sum(scores.values())}")

        return sum(scores.values())

    @staticmethod
    def _read_input(fn: str) -> dict:
        """Reads in the txt file and returns the list of cards."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        cards = {}
        for line in raw_data:
            card_idx = line.split('Card ')[1].split(':')[0]
            win_nums = [int(num) for num in line.split(': ')[1].split(' |')[0].split()]
            my_nums = [int(num) for num in line.split('| ')[1].split()]
            cards.update({card_idx: {'win_nums': win_nums, 'my_nums': my_nums}})

        return cards


if __name__ == '__main__':
    test_file = 'test-input.txt'
    test_solver = PuzzleSolver(test_file)
    test_solution = test_solver.solve()

    real_file = 'input.txt'
    real_solver = PuzzleSolver(real_file)
    real_solution = real_solver.solve(show_matching=True)
