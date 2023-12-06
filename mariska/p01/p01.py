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


def day1(calibration_file):
    matching_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    total1 = get_sum_of_first_and_last_digit(calibration_file, matching_numbers)
    matching_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six",
                        "seven", "eight", "nine"]
    total2 = get_sum_of_first_and_last_digit(calibration_file, matching_numbers)
    return total1, total2

if __name__ == "__main__":
    print(day1(open("01.txt").readlines()))