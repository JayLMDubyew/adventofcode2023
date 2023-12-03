import re
from pathlib import Path
from collections import defaultdict


def get_gear_ratios(problem_lines):
    gear_dict = generate_gear_dict(problem_lines)
    print(gear_dict)

def get_part_count(problem_lines):
    symbol_dict = generate_symbol_dict(problem_lines)
    part_number_sum = 0

    line_number = 0
    for line in problem_lines:
        findings = re.finditer(r'(\d+)',line)
        for finding in findings:
            is_part = False
            part_number = finding.groups()[0]
            left = finding.span()[0]
            right = finding.span()[1]
            for index in range(left, right):
                #left
                if index-1 in symbol_dict[line_number]:
                    is_part = True
                #right
                elif index+1 in symbol_dict[line_number]:
                    is_part = True
                #up
                elif index in symbol_dict[line_number-1]:
                    is_part = True
                #down
                elif index in symbol_dict[line_number+1]:
                    is_part = True
                #up-left
                elif index-1 in symbol_dict[line_number-1]:
                    is_part = True
                #up-right
                elif index+1 in symbol_dict[line_number-1]:
                    is_part = True
                #down-left
                elif index-1 in symbol_dict[line_number+1]:
                    is_part = True
                #down-right
                elif index+1 in symbol_dict[line_number+1]:
                    is_part = True
            if is_part:
                part_number_sum += int(part_number)
        line_number += 1


    return part_number_sum
def is_special(character):
    return not character.isdigit() and character != '.' and character != '\n'

def is_gear(character):
    return character == '*'

def generate_gear_dict(problem_lines):
    symbol_dict = defaultdict(set)
    line_number = 0
    for line in problem_lines:
        x = 0
        for character in line.rstrip():
            if is_gear(character):
                symbol_dict[line_number].add(x)
            x += 1
        line_number += 1
    return symbol_dict
def generate_symbol_dict(problem_lines):
    symbol_dict = defaultdict(set)
    line_number = 0
    for line in problem_lines:
        x = 0
        for character in line.rstrip():
            if is_special(character):
                symbol_dict[line_number].add(x)
            x += 1
        line_number += 1
    return symbol_dict

class Day3:
    def __init__(self):
        self.problem_input_location = Path('../puzzle_input/3.txt')

    def print_problem(self):
        with open(self.problem_input_location, 'r') as problem:
            problem_lines = problem.readlines()
        print(f'Part 1: {self.part_1(problem_lines)} \n')
        print(f'Part 2: {self.part_2(problem_lines)} \n')

    def part_1(self, problem_lines):
        return get_part_count(problem_lines)


    def part_2(self, problem_lines):
        get_gear_ratios(problem_lines)
        return 0


day3 = Day3()
day3.print_problem()
