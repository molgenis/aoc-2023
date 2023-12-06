import re


def is_symbol(character):
    return not character.isnumeric() and character != "."


def is_symbol_around(matches, line, line_number, engine_data):
    start_index = matches.start()
    stop_index = matches.end()
    index_before = start_index - 1 if not is_first(start_index) else 0
    index_after = stop_index + 1 if not is_last(start_index, len(line)) else stop_index
    symbol_found = False
    if is_symbol_before(start_index, line) or is_symbol_after(stop_index, line):
        symbol_found = True
    if not is_first(line_number):
        diagonal_vertical_above = get_characters_in_line_above(engine_data, line_number, index_before, index_after)
        if is_symbol_on_vertical_diagonal(diagonal_vertical_above):
            symbol_found = True
    if not is_last(line_number, len(line) - 1):
        diagonal_vertical_below = get_characters_in_line_below(engine_data, line_number, index_before, index_after)
        if is_symbol_on_vertical_diagonal(diagonal_vertical_below):
            symbol_found = True
    if symbol_found:
        return True
    else:
        return False


def get_full_number(line, index):
    regex = r'\d+'
    matches = re.finditer(regex, line)
    numbers = []
    for match in matches:
        start = match.start()
        end = match.end()
        if start <= index <= end or start <= index + 1 <= end:
            numbers.append(int(match.group(0)))
    return numbers


def get_gear_info(matches, line, line_number, data):
    index = matches.start()
    index_before = index - 1 if not is_first(index) else 0
    index_after = index + 1 if not is_last(index, len(line)) else index
    numbers = []
    if (index_before != 0 and line[index_before].isnumeric()) or \
            (index_after != index and line[index_after].isnumeric()):
        numbers += get_full_number(line, index)
    if not is_first(line_number):
        numbers += get_full_number(data[line_number - 1], index)
    if not is_last(line_number, len(line) - 1):
        numbers += get_full_number(data[line_number + 1], index)
    return numbers


def get_character_before(index, line):
    return line[index - 1]


def is_symbol_before(start_index, line):
    return is_symbol(get_character_before(start_index, line)) if not is_first(start_index) else False


def is_symbol_after(stop_index, line):
    return is_symbol(line[stop_index]) if not is_last(stop_index, len(line)) else False


def is_symbol_on_vertical_diagonal(diagonal_vertical):
    for character in diagonal_vertical:
        if is_symbol(character):
            return True
    return False


def get_characters_in_line_above(data, line_number, index_before, index_after):
    return data[line_number - 1].strip("\n")[index_before:index_after]


def get_characters_in_line_below(data, line_number, index_before, index_after):
    return data[line_number + 1].strip("\n")[index_before:index_after]


def is_last(index, length):
    return index == length


def is_first(index):
    return index == 0


def day3(engine_data):
    total = 0
    gear_ratio_sum = 0
    for line_number, line in enumerate(engine_data):
        line = line.strip("\n")
        numbers = re.finditer(r'\d+', line)
        gears = re.finditer(r'\*', line)
        for matches in numbers:
            number = matches.group(0)
            symbol_found = is_symbol_around(matches, line, line_number, engine_data)
            if symbol_found:
                total += int(number)
        for matches in gears:
            numbers = get_gear_info(matches, line, line_number, engine_data)
            if len(numbers) == 2:
                gear_ratio_sum += get_gear_ratio(numbers)
    return total, gear_ratio_sum


def get_gear_ratio(numbers):
    return numbers[0] * numbers[1]


if __name__ == "__main__":
    print(day3(open("03.txt").readlines()))