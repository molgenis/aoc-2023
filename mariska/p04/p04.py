def is_match(my_number, winning):
    return my_number in winning
    

def process_line(line):
    card = line.strip("\n").split(": ")
    card_number = int(card[0].replace("Card", "").strip())
    scratch_data = card[1].split(" | ")
    winning = scratch_data[0].strip().split(" ")
    my_card = list(filter(None, scratch_data[1].split(" ")))
    return card_number, winning, my_card


def make_copy(card_number, copies):
    if card_number not in copies:
        copies[card_number] = 1
    else:
        copies[card_number] += 1
    return copies


def process_card(my_card, winning, card_number, winning_matches, copies_of_cards):
    winning_matches = 0
    for my_number in my_card:
        match = is_match(my_number, winning)
        if match:
            winning_matches += 1
            copies_of_cards = make_copy(card_number + winning_matches, copies_of_cards)
    return winning_matches, copies_of_cards


def day4(scratchcards):
    overall_score = 0
    number_of_cards = 0
    copies_of_cards = {}
    for line in scratchcards:
        card_number, winning, my_card = process_line(line)
        winning_matches = 0
        winning_matches, copies_of_cards = process_card(my_card, winning, card_number, winning_matches, copies_of_cards)
        if card_number in copies_of_cards:
            for copy in range(copies_of_cards[card_number]):
                winning_matches, copies_of_cards = process_card(my_card, winning, card_number, winning_matches, copies_of_cards)

        if winning_matches > 0:
            score = 2 ** (winning_matches - 1)
            overall_score += score
    number_of_cards = sum(list(copies_of_cards.values())) + len(scratchcards)
    return overall_score, number_of_cards

if __name__ == "__main__":
    print(day4(open("04.txt").readlines()))