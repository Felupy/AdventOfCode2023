import sys
import os

INPUT_FILE = "input.txt"
NUMBERS_STR = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


#################
### FUNCTIONS ###
#################
      
def find_numbers(line:str):
    first_num = "0"
    last_num = "0"

    first_num = find_num(line, False)
    last_num = find_num(line, True)

    return first_num, last_num
    

def find_num(line:str, reverse:bool):
    partial_str = ""
    num_str = ""

    if reverse:
        line = line[::-1] # invert the line

    for c in line:
        if c.isdigit():
            return c
        else:

            if reverse:
                partial_str = c + partial_str
            else:
                partial_str += c
    
            # check if partial str is a str number
            if len(partial_str) >= 3:
                for idx, word in enumerate(NUMBERS_STR):
                    if word in partial_str:
                        return str(idx + 1)
                
    return "0"
        

############
### MAIN ###
############

print(f"Processing file: {INPUT_FILE}")

numbers_detected = []
with open(INPUT_FILE, 'r') as f:
    for line in f:
        first_num, last_num = find_numbers(line)
        # print(f"First: {first_num} \ Last: {last_num}")
        numbers_detected.append(int(''.join([first_num, last_num])))


calibration_value = sum(numbers_detected)
print(f"Calibration value: {calibration_value}")  
