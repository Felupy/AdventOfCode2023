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
    id = fields[0].split(' ')
    numbers_fields = fields[1].split('|')
    wn = [int(n) for n in numbers_fields[0].strip().split(' ')]
    an =  [int(n) for n in numbers_fields[1].strip().split(' ')]


    return Card(id, wn, an)

def analyze_card(c: Card):
    card_points = 0
    for number in c.winner_numbers:
        if number in c.available_numbers:
            if card_points == 0:
                card_points = 1
            else:
                card_points *= 2
    
    return card_points
    

############
### MAIN ###
############

print(f"Processing file: {INPUT_FILE}")

cards=[]
total_points = 0
with open(INPUT_FILE, 'r') as f:
    for line in f:
        cards.append(process_card(line))

    for c in cards:
        points = analyze_card(c)
        total_points += points
        


print(f"=> Result: {total_points}")  