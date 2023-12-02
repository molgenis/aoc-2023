# Functions for day 1:
def concatenate_numbers(number1, number2):
    return str(number1) + str(number2)


def find_first_and_last(string, items_to_find):
    first_index = len(string)
    last_index = 0
    first_item = ""
    last_item = ""
    for item in items_to_find:
        try:
            found_index = string.index(item)
            found_rindex = string.rindex(item)
            if found_index <= first_index:
                first_index = found_index
                first_item = item
            if found_rindex <= first_index:
                first_index = found_rindex
                first_item = item
            if found_index >= last_index:
                last_index = found_index
                last_item = item
            if found_rindex >= last_index:
                last_index = found_rindex
                last_item = item
        except ValueError:
            # Nothing's wrong. The item is just not in the string and python's being dramatic.
            pass
    return first_item, last_item


def string_number_to_int(number):
    numbers_as_text = {"one": "1",
                       "two": "2",
                       "three": "3",
                       "four": "4",
                       "five": "5",
                       "six": "6",
                       "seven": "7",
                       "eight": "8",
                       "nine": "9"}
    if number in numbers_as_text.keys():
        return int(numbers_as_text[number])
    else:
        return int(number)


def get_sum_of_first_and_last_digit(calibration_file, matching_numbers):
    total = 0
    for line in calibration_file:
        first, last = find_first_and_last(line, matching_numbers)
        first_number = string_number_to_int(first)
        last_number = string_number_to_int(last)
        number = concatenate_numbers(first_number, last_number)
        total += int(number)
    return total


def day1(input_file):
    calibration_file = open_file(input_file)
    matching_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    total1 = get_sum_of_first_and_last_digit(calibration_file, matching_numbers)
    matching_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six",
                        "seven", "eight", "nine"]
    total2 = get_sum_of_first_and_last_digit(calibration_file, matching_numbers)
    print_my_answer("1", "Sum of calibration values", total1, "Sum of calibration values", total2)


# Functions for day 2:
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


def day2(input_file):
    game_data = open_file(input_file)
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
    print_my_answer("2", "Sum of ID's for possible games", sum_of_ids, "Sum of powers", sum_of_powers)


# Functions for all days:
def print_my_answer(day, part1_msg, part1_ans, part2_msg, part2_ans):
    print(f"DAY: {day}\n part 1:\n  {part1_msg}: {part1_ans}\n part 2:\n  {part2_msg}: {part2_ans}\n")


def open_file(input_file):
    return open(input_file).readlines()


if __name__ == '__main__':
    input_day1 = "input_files/input_day1.txt"
    day1(input_day1)
    input_day2 = "input_files/input_day2.txt"
    day2(input_day2)
