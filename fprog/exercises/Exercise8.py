#!/usr/bin/python3

def count_steps_collatz_conjecture(initial_number: int) -> int:
    steps_taken = 0
    number_tracked = initial_number

    while number_tracked > 1:
        if number_tracked % 2 == 0: # Even
            number_tracked //= 2
        else: # Odd
            number_tracked = 3 * number_tracked + 1
        steps_taken += 1

    return steps_taken

# Get input from user
number_start = input("Enter starting number: ")

# Validate number_start
if not number_start.isdigit():
    raise ValueError("Invalid number.")

number_end = input("Enter ending number: ")

# Validate number_end
if not number_end.isdigit():
    raise ValueError("Invalid number.")

number_start = int(number_start)
number_end = int(number_end)

if number_start > number_end:
    raise ValueError("Starting number can't be greater than the ending number!")

for i in range(number_start, number_end + 1):
    collatz_result = count_steps_collatz_conjecture(i)
    print(f"{i} {collatz_result}")