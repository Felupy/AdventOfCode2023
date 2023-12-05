import sys
import os

INPUT_FILE = "input.txt"
MAX_RED_CUBES = 12
MAX_BLUE_CUBES = 14
MAX_GREEN_CUBES = 13
CUBES_MAX_COLOR_DICT = {"blue":MAX_BLUE_CUBES, "red":MAX_RED_CUBES, "green":MAX_GREEN_CUBES}

# Ex: Line = Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def check_game(line:str):
    id = 0
    fields = line.split(':')
    id = int(fields[0].split(' ')[1])

    # Ex: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    combinations = fields[1].split(';')

    for combi in combinations:
        # Ex: 1 red, 2 green, 6 blue
        hands = combi.split(',')
        for cubes in hands:
            # Ex: 3 blue
            values = cubes.strip().split(' ')
            num_cubes = int(values[0])
            color = values[1]

            if num_cubes > CUBES_MAX_COLOR_DICT[color]:
                return False, id

    return True, id


############
### MAIN ###
############

print(f"Processing file: {INPUT_FILE}")

games_possible = []
with open(INPUT_FILE, 'r') as f:
    for line in f:
        isPossible, id = check_game(line)
        if isPossible:
            games_possible.append(id)
        


result = sum(games_possible)
print(f"=> Result: {result}")  