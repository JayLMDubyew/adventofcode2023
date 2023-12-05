from collections import defaultdict
from pathlib import Path
import re

# yeah yeah i know the style changed. sue me, i'm sick as a dog but i wanted to get this done.
problem_input_location = Path('../puzzle_input/4.txt')

with open(problem_input_location, 'r') as problem_input:
    problem_lines = problem_input.readlines()


def part1():
    total_score = 0
    for cardset in problem_lines:
        score = 0
        cardset = cardset.rstrip().split("|")
        winning_cards = cardset[0].split(":")[1].split()
        cards_i_have = cardset[1].split()

        for card in cards_i_have:
            if card in winning_cards:
                score = max(1, score * 2)
        total_score += score
    print(total_score)


def part2():
    card_dict = defaultdict(int)
    total_card_dict = defaultdict(int)
    num_cards = len(problem_lines)
    for cardset in problem_lines:
        cardset = cardset.rstrip().split("|")
        card_number = int(cardset[0].split(":")[0].split()[1])
        card_dict[card_number] = 0
        winning_cards = cardset[0].split(":")[1].split()
        cards_i_have = cardset[1].split()
        # print(card_number)
        for card in cards_i_have:

            if card in winning_cards:
                card_dict[card_number] += 1
    print(card_dict)
    total_cards = 0

    print(total_card_dict)


part2()
