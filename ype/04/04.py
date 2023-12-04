"""
Script to solve the fourth puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/4
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.data = self._read_input(filename)

    def solve_part_1(self, show_matching: bool = False) -> int:
        """Solves the first part of the puzzle."""
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

        print("The score of each card equals: ")
        for card, score in scores.items():
            print(f"{card:3}: {score}")

        print(f"The total score equals: {sum(scores.values())}")

        return sum(scores.values())

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""
        scores = {
            card: len(list(set(numbers['win_nums']) & set(numbers['my_nums'])))
            for card, numbers in self.data.items()
        }

        copies = {card: 1 for card in scores.keys()}

        for card, s in scores.items():
            if s == 0:
                continue
            c = copies[card]
            for i in range(1, s+1):
                copies[card+i] += c

        cards_total = sum(copies.values())
        print(f"Total number of cards: {cards_total}.")
        
        return cards_total

    @staticmethod
    def _read_input(fn: str) -> dict:
        """Reads in the txt file and returns the list of cards."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        cards = {}
        for line in raw_data:
            card_idx = int(line.split('Card ')[1].split(':')[0])
            win_nums = [int(num) for num in line.split(': ')[1].split(' |')[0].split()]
            my_nums = [int(num) for num in line.split('| ')[1].split()]
            cards.update({card_idx: {'win_nums': win_nums, 'my_nums': my_nums}})

        return cards


if __name__ == '__main__':
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    test_solution_1 = test_solver.solve_part_1()
    test_solution_2 = test_solver.solve_part_2()

    real_file = '04.txt'
    real_solver = PuzzleSolver(real_file)
    real_solution_1 = real_solver.solve_part_1()
    real_solution_2 = real_solver.solve_part_2()
