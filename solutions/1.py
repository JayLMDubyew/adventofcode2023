from pathlib import Path

class Day1:
    def __init__(self):
        self.problem_input_location = Path('../puzzle_input/1.txt')

    def print_problem(self):
        with open(self.problem_input_location, 'r') as problem:
            print(problem.read())

day1 = Day1()
day1.print_problem()
