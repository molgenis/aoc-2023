import utils, os
from p01.p01 import day1
from p02.p02 import day2
from p03.p03 import day3
from p04.p04 import day4


if __name__ == '__main__':
    # Make sure you are in the "mariska" directory when running this
    input_day1 = utils.open_file("p01/01.txt")
    part1, part2 = day1(input_day1)
    utils.print_my_answer("1", "Sum of calibration values", part1, "Sum of calibration values", part2)
    
    input_day2 = utils.open_file("p02/02.txt")
    part1, part2 = day2(input_day2)
    utils.print_my_answer("2", "Sum of ID's for possible games", part1, "Sum of powers", part2)
    
    input_day3 = utils.open_file("p03/03.txt")
    part1, part2 = day3(input_day3)
    utils.print_my_answer("3", "Sum of engine part numbers", part1, "Sum of gear ratios", part2)

    input_day4 = utils.open_file("p04/04.txt")
    part1, part2 = day4(input_day4)
    utils.print_my_answer("4", "Overall score", part1, "Number of cards", part2)