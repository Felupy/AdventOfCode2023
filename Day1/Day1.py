import sys
import os

input_file = "input.txt"

print(f"Processing file: {input_file}")

numbers_detected = []
with open(input_file, 'r') as f:
    for line in f:
        numbers = list(filter(str.isdigit, line))
        if numbers:
            numbers_detected.append(int(''.join([numbers[0],numbers[-1]])))


print(numbers_detected)

calibration_value = sum(numbers_detected)
print(f"Calibration value: {calibration_value}")  
