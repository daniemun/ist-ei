#!/usr/bin/python3

# Get input from user
numberA = input("Enter number A: ")

# Validate Number A
if not numberA.isdigit():
    raise ValueError("Invalid number.")
    
numberA = int(numberA)

numberB = input("Enter number B: ")

# Validate Number B
if not numberB.isdigit():
    raise ValueError("Invalid number.")
    
numberB = int(numberB)

# Output calculations
print(f"A + B = {numberA + numberB}")
print(f"A - B = {numberA - numberB}")
print(f"A * B = {numberA * numberB}")