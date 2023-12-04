def print_my_answer(day, part1_msg, part1_ans, part2_msg, part2_ans):
    print(f"DAY: {day}\n part 1:\n  {part1_msg}: {part1_ans}\n part 2:\n  {part2_msg}: {part2_ans}\n")


def open_file(input_file):
    return open(input_file).readlines()