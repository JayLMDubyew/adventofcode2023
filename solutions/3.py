import re
from pathlib import Path
from collections import defaultdict


def get_part_numbers(problem_lines):
    part_dict = defaultdict(int)

    parts_sum = 0
    number_re = r'(\d+)'
    index = 0
    num_lines = len(problem_lines)
    for line in problem_lines:
        line = line.rstrip()
        line_len = len(line)
        matches = re.finditer(number_re, line)

        for match in matches:
            match_is_part = False
            left_bound = match.span()[0]
            right_bound = match.span()[1]
            # ANYTHING adjacent to a symbol is a part.
            # up-left, up-right, left, right, down-left, down-right, up, down


            for i in range(left_bound,right_bound,1):
                # up
                if index > 0 and (not problem_lines[index - 1][i].isnumeric()) and (
                        problem_lines[index - 1][i] != '.'):
                    match_is_part = True

                #down
                if index + 1 < num_lines and (not problem_lines[index + 1][i].isnumeric()) and (
                        problem_lines[index +1][i] != '.'):
                    match_is_part = True


                if i > 0:
                    # up-left
                    if index > 0 and (not problem_lines[index - 1][i - 1].isnumeric()) and (
                            problem_lines[index - 1][i - 1] != '.'):
                        match_is_part = True
                    # left
                    if (not problem_lines[index][i - 1].isnumeric()) and (
                            problem_lines[index][i - 1] != '.'):
                        match_is_part = True
                    # down-left
                    if index + 1 < num_lines and (not problem_lines[index - 1][i - 1].isnumeric()) and (
                            problem_lines[index + 1][i - 1] != '.'):
                        match_is_part = True

                    # up-right
                if right_bound + 1 < line_len:
                    if index > 0 and (not problem_lines[index - 1][i].isnumeric()) and (
                            problem_lines[index - 1][i] != '.'):
                        match_is_part = True
                    # right

                    if (not problem_lines[index][i].isnumeric()) and (
                            problem_lines[index][i] != '.'):
                        match_is_part = True
                    # down-right
                    if index + 1 < num_lines and (not problem_lines[index + 1][i].isnumeric()) and (
                            problem_lines[index + 1][i] != '.'):
                        match_is_part = True

            print(match.groups()[0], match_is_part)
            if match_is_part:
                parts_sum += int(match.groups()[0])
        index += 1
    return parts_sum


class Day3:
    def __init__(self):
        self.problem_input_location = Path('../puzzle_input/3.txt')

    def print_problem(self):
        with open(self.problem_input_location, 'r') as problem:
            problem_lines = problem.readlines()
        print(f'Part 1: {self.part_1(problem_lines)} \n')
        print(f'Part 2: {self.part_2(problem_lines)} \n')

    def part_1(self, problem_lines):
        return get_part_numbers(problem_lines)


    def part_2(self, problem_lines):
        return 0


day3 = Day3()
day3.print_problem()
