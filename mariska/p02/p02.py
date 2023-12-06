def extract_game_id(line_part):
    return int(line_part.replace("Game ", ""))


def get_min_amount_of_cubes_in_game(game_data):
    min_amount_of_colours = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for round in game_data:
        for col_info in round.split(', '):
            amount, colour = col_info.split(" ")
            if int(amount) > min_amount_of_colours[colour]:
                min_amount_of_colours[colour] = int(amount)
    return min_amount_of_colours


def is_game_possible_with_expected(expected, actual):
    for colour, amount in expected.items():
        if actual[colour] > expected[colour]:
            return False
    return True


def get_power_of_amounts(amounts):
    power = 1
    for amount in amounts.values():
        power = amount * power
    return power


def day2(game_data):
    sum_of_ids = 0
    sum_of_powers = 0
    for line in game_data:
        line = line.strip("\n").split(": ")
        game_id = extract_game_id(line[0])
        game_input = line[1].split("; ")
        expected_amounts = {
            "red": 12,
            "blue": 14,
            "green": 13
        }
        min_amounts = get_min_amount_of_cubes_in_game(game_input)
        is_possible = is_game_possible_with_expected(expected_amounts, min_amounts)
        if is_possible:
            sum_of_ids += game_id
        power = get_power_of_amounts(min_amounts)
        sum_of_powers += power
    return sum_of_ids, sum_of_powers

if __name__ == "__main__":
    print(day2(open("02.txt").readlines()))