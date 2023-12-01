from pathlib import Path
import re
from word2number import w2n


def convert_text_to_number(line):
    pairs = [('one', 'o1e'), ('two', 't2'), ('three', 't3e'), ('four', '4'), ('five', '5e'), ('six', '6'),
             ('seven', '7n'), ('eight', 'e8t'), ('nine', 'n9e')]
    for text, numeric in pairs:
        line = line.replace(text, numeric)
    return line


def get_first_and_last(line):
    line_matches = re.findall(r'\d', line)
    first = line_matches[0]
    last = line_matches[-1]
    return int(first + last)


class Day1:
    def __init__(self):
        self.problem_input_location = Path('../puzzle_input/1.txt')

    def print_problem(self):
        with open(self.problem_input_location, 'r') as problem:
            problem_lines = problem.readlines()
        print(f'Part 1: {self.part_1(problem_lines)} \n')
        print(f'Part 2: {self.part_2(problem_lines)} \n')

    def part_1(self, problem):
        # get first and last digit on each line
        total = 0
        for line in problem:
            total += get_first_and_last(line)
        return total

    def part_2(self, problem):
        total = 0
        for line in problem:
            line = convert_text_to_number(line)
            total += get_first_and_last(line)
        return total


day1 = Day1()
day1.print_problem()
