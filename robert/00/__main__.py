#!/usr/bin/env python3

import os
import argparse
from pathlib import Path


def main():
    input_path = CommandLineParser().get_input()
    input_data = FileReader().read_txt_file(input_path)
    counter = Counter()
    answer_part_1 = counter.count(input_data, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    answer_part_2 = counter.count(
        input_data,
        ['1', '2', '3', '4', '5', '6', '7', '8', '9',
         'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
         ]
    )
    print(f"Final answer part 1: {answer_part_1}")
    print(f"Final answer part 2: {answer_part_2}")


class Counter:
    def count(self, input_data, items_of_interest):
        counts = 0
        for line in input_data:
            if line != "":
                first, last = self._first_and_last_obtainor(line, items_of_interest)
                first_number = self._number_corrector(first)
                last_number = self._number_corrector(last)
                counts += int(f"{first_number}{last_number}")
        return counts

    @staticmethod
    def _first_and_last_obtainor(input_data_line, items_of_interest):
        first_index = len(input_data_line)
        last_index = 0
        first_item = ""
        last_item = ""
        for item in items_of_interest:
            try:
                lindex = input_data_line.index(item)
                rindex = input_data_line.rindex(item)
                if lindex <= first_index:
                    first_index = lindex
                    first_item = item
                if rindex <= first_index:
                    first_index = rindex
                    first_item = item
                if lindex >= last_index:
                    last_index = lindex
                    last_item = item
                if rindex >= last_index:
                    last_index = rindex
                    last_item = item
            except ValueError:
                pass
        return first_item, last_item

    @staticmethod
    def _number_corrector(number):
        number_replacements = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        if number in number_replacements.keys():
            return int(number_replacements[number])
        else:
            return int(number)


class FileReader:
    @staticmethod
    def read_txt_file(path):
        with open(path) as input_file:
            input_data = input_file.readlines()
        return input_data


class CommandLineParser:
    def __init__(self):
        self.cli = CommandLineInterpreter()

    def get_input(self):
        input_file = Path(self.cli.get_argument("input")).absolute()
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file {input_file} not found.")
        return input_file


class CommandLineInterpreter:
    def __init__(self):
        self.arguments = self._create_argument_parser().parse_args()

    @staticmethod
    def _create_argument_parser():
        parser = argparse.ArgumentParser(
            prog="Day 0 Advent of Code 2023 script",
            description="Providing the sum of all lines in a given file, adding together the first and last number of"
                        " a line."
        )

        required = parser.add_argument_group("Required")
        required.add_argument(
            "-i",
            "--input",
            type=str,
            required=True,
            help="The location of the input file."
        )
        return parser

    def get_argument(self, argument_key):
        if argument_key in self.arguments:
            return getattr(self.arguments, argument_key)
        else:
            raise KeyError(f"Argument {argument_key} invalid, not found in CLI arguments.")


if __name__ == "__main__":
    main()
