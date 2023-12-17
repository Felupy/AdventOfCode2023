import sys
import os
import re
from card import *

INPUT_FILE = "input.txt"


def process_card(line: str):
    
    # Line format:
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    line = line.replace("  ", " ")
    fields = line.split(':')
    id = int(fields[0].replace("  ", " ").split(' ')[1])
    numbers_fields = fields[1].strip().split('|')
    wn = [int(n) for n in numbers_fields[0].strip().split(' ')]
    an =  [int(n) for n in numbers_fields[1].strip().split(' ')]

    return Card(id, wn, an)

def process_card_copies(card_dict, card_id):
    card_win_numbers = card_dict[card_id]
    matchs = len(card_win_numbers)
    if matchs > 0:
        card_copies = 1
        for i in range(matchs):
            card_copies += process_card_copies(card_dict, card_id + i + 1)
            # print(f"Card {card_id} - {card_copies}")
        return card_copies
    else:
        return 1
    



############
### MAIN ###
############

print(f"Processing file: {INPUT_FILE}")

cards=[]
card_matchs_dict = {}
card_copies_dict = {}
with open(INPUT_FILE, 'r') as f:
    for line in f:
        cards.append(process_card(line))

    for c in cards:
        matching_numbers = c.get_matching_numbers()
        # print(f"Card {c.id}: {matching_numbers}")
        card_matchs_dict[c.id] = matching_numbers

    for key, value in card_matchs_dict.items():
        copies = process_card_copies(card_matchs_dict, key)
        # print(f"Copies(Card {key}): {copies}")
        card_copies_dict[key] = copies



        


print(f"=> Result: {sum(card_copies_dict.values())}")  