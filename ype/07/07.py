"""
Script for solving the seventh puzzle of the Advent of Code 2023 competition.
https://adventofcode.com/2023/day/7
"""


class PuzzleSolver:
    """Object to solve a puzzle."""

    def __init__(self, filename: str):
        """Initializes the object by reading in the file."""
        self.hands: dict = self._read_input(filename)
        self.strengths = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def solve_part_1(self) -> int:
        """Solves the first part of the puzzle.

        The reasoning is as follows:
        before the winnings can be multiplied by their respective ranks, the ordering of the
        strength of the hands must be determined.
        This is done by comparing the unique code that is assigned to each hand, consisting of the
        numerical representation of the hand type, followed by a string of numerical representation
        of each card strength.
        """

        # Find the types and create a score code for each hand
        hand_types = {}
        for hand, bid in self.hands.items():
            # Count the occurrences of each strength in the hand and sort the occurrences in descending order
            ch_counts = sorted(map(lambda ch: hand.count(ch), set(hand)), reverse=True)

            # Using these counts, class the hand as one of the seven types (7: five of a kind, ..., 0: high card)
            if ch_counts[0] > 3:
                # Five or four of a kind
                h_type = ch_counts[0]+1
            elif ch_counts[0] == 3:
                # Three of a kind
                h_type = 3
                if ch_counts[1] == 2:
                    # Full house
                    h_type += 1
            elif ch_counts[1] == 2:
                # Two pair
                h_type = 2
            elif ch_counts[0] == 2:
                # One pair
                h_type = 1
            else:
                # High card
                h_type = 0

            # Create a unique score code for each card, consisting of the hand type value and the value of each card
            score_code = str(h_type) + ''.join(map(lambda card:
                                                   str(self.strengths.get(hand[card], hand[card])).rjust(2, '0'),
                                                   range(len(hand))))
            hand_types[score_code] = int(bid)

        # Sort the bids based on the hand scores
        ordered_bids = {key: hand_types.copy()[key] for key in sorted(hand_types.keys())}

        # Tally the winnings of the bids
        winnings = 0
        for rank, bid in zip(range(1, len(ordered_bids)+1), ordered_bids.values()):
            winnings += rank * bid

        print(f"The total winnings are {winnings}.")

        return winnings

    def solve_part_2(self) -> int:
        """Solves the second part of the puzzle."""

    @staticmethod
    def _read_input(fn: str) -> dict:
        """Reads in the txt file and returns a dictionary of the hands and bids."""
        with open(file=fn) as f:
            raw_data = f.readlines()

        hands = {line.split()[0]: line.split()[1] for line in raw_data}

        return hands


if __name__ == '__main__':
    print(f"Test solutions")
    test_file = 't1.txt'
    test_solver = PuzzleSolver(test_file)
    print(f"\nSolution for part 1")
    test_solution_1 = test_solver.solve_part_1()
    print(f"\nSolution for part 2")
    test_solution_2 = test_solver.solve_part_2()

    print(f"\n\nReal solutions")
    real_file = '07.txt'
    real_solver = PuzzleSolver(real_file)
    print(f"\nSolution for part 1")
    real_solution_1 = real_solver.solve_part_1()
    print(f"\nSolution for part 2")
    real_solution_2 = real_solver.solve_part_2()
