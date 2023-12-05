import sys
import os
import re

INPUT_FILE = "input.txt"

def check_if_symbol_around_num(map, num_str:str, row_index:int, c_indx:int, digit_len:int, max_rows:int, max_columns:int):

    min_row = 0
    max_row = 0
    min_column = 0
    max_column = 0


    # check map limits
    if row_index == 0:
        min_row = row_index
        max_row = row_index + 1
    elif row_index == (max_rows - 1):
        min_row = row_index - 1
        max_row = row_index
    else:
        min_row = row_index - 1
        max_row = row_index + 1

    # check map for columns. c_indx is the index following the number, so no need to +1
    if c_indx == 0:
        min_column = c_indx - (digit_len)
        max_column = c_indx 
    elif c_indx == (max_columns):
        min_column = c_indx - (digit_len) - 1
        max_column = c_indx - 1
    else:
        min_column = c_indx - (digit_len) - 1
        max_column = c_indx 

    print(f"Num: {num_str}")
    print(f"Map: [{min_row},{max_row}]")
    print(f"     [{min_column},{max_column}]")

    # look around coordinates
    for i in range(min_row, max_row+1):
        for j in range(min_column, max_column+1):
            cell_value = map[i][j]
            if not cell_value.isdigit():
                if cell_value != ".":
                    return True



    return False

def process_schematic(schematic):

    schematic_rows = len(schematic)
    schematic_columns = len(schematic[0])
    part_numbers = []
    
    for row_indx, row in enumerate(schematic):
        num_str = ""
        for c_indx, c in enumerate(row):
            if c.isdigit():
                num_str += c
            else:
                if num_str != "":
                    print(f"C_index:{c_indx}")
                    symbol_around = check_if_symbol_around_num(schematic, num_str, row_indx, c_indx, len(num_str), schematic_rows, schematic_columns)
                    if symbol_around:
                        print(symbol_around)
                        part_numbers.append(int(num_str))
                    num_str = ""





    return part_numbers



############
### MAIN ###
############

print(f"Processing file: {INPUT_FILE}")

engine_schematic=[]
with open(INPUT_FILE, 'r') as f:
    for line in f:
        engine_schematic.append(line)

    part_numbers = process_schematic(engine_schematic)    
        


result = sum(part_numbers)
print(f"=> Result: {result}")  