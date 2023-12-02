from pathlib import Path
import re


class Day2:
    def __init__(self):
        self.problem_input_location = Path('../puzzle_input/2.txt')
        self.theoretical_cubes = {'red': 0, 'blue': 0, 'green': 0}

    def print_problem(self):
        with open(self.problem_input_location, 'r') as problem:
            problem_lines = problem.readlines()
        print(f'Part 1: {self.part_1(problem_lines)}')
        print(f'Part 2: {self.part_2(problem_lines)}')

    def part_1(self, problem_lines):
        self.theoretical_cubes['red'] = 12
        self.theoretical_cubes['green'] = 13
        self.theoretical_cubes['blue'] = 14

        possible_game_sum = 0

        for line in problem_lines:
            game_number = int(re.search(r'Game (\d+):', line)[1])
            individual_games = line.split(';')
            game_is_possible = True
            for game in individual_games:
                num_red = re.search(r'(\d+) red', game)
                num_green = re.search(r'(\d+) green', game)
                num_blue = re.search(r'(\d+) blue', game)

                if not num_red:
                    num_red = 0
                else:
                    num_red = int(num_red[1])

                if not num_green:
                    num_green = 0
                else:
                    num_green = int(num_green[1])

                if not num_blue:
                    num_blue = 0
                else:
                    num_blue = int(num_blue[1])

                if not ((self.theoretical_cubes['red'] - num_red > -1) and (self.theoretical_cubes['green'] - num_green > -1) and (self.theoretical_cubes['blue'] - num_blue > -1)):
                    game_is_possible = False
            if game_is_possible:
                possible_game_sum += game_number
        return  possible_game_sum

    def part_2(self, problem_lines):

        the_power = 0

        for line in problem_lines:
            individual_games = line.split(';')
            red_power = 0
            green_power = 0
            blue_power = 0
            for game in individual_games:
                num_red = re.search(r'(\d+) red', game)
                num_green = re.search(r'(\d+) green', game)
                num_blue = re.search(r'(\d+) blue', game)

                if not num_red:
                    num_red = 1
                else:
                    num_red = int(num_red[1])

                if not num_green:
                    num_green = 1
                else:
                    num_green = int(num_green[1])

                if not num_blue:
                    num_blue = 1
                else:
                    num_blue = int(num_blue[1])
                red_power = max(num_red,red_power)
                blue_power = max(num_blue,blue_power)
                green_power = max(num_green,green_power)

            game_power = red_power * blue_power * green_power
            the_power += game_power


        return the_power


day2 = Day2()
day2.print_problem()
