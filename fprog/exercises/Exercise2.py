#!/usr/bin/python3

# Get input from user
number = input("Enter a number: ")

# Validate and convert when input is valid
if not number.isdigit():
    raise ValueError("Invalid number.")

number = int(number)
    
# Check if it's odd
if number % 2 != 0:
    print("Estranho")
else: # Else it's even
    if number >= 2 and number <= 5:
        print("Não é estranho")
    elif number >= 6 and number <= 20:
        print("Estranho")
    elif number > 20:
        print("Não é estranho")