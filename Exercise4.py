#!/usr/bin/env python

# Get input from user
n_many = input("Enter the bigger number (n_many): ")

# Validate n_many
if not n_many.isdigit():
    raise ValueError("Invalid number.")
    
n_many = int(n_many)

n_divisor = input("Enter the divisor (n_divisor): ")

# Validate n_divisor
if not n_divisor.isdigit():
    raise ValueError("Invalid number.")
    
n_divisor = int(n_divisor)

# From 0 to n_many, print only the ones not divisible by n_divisor
for i in range(n_many):
    if i % n_divisor != 0:
        print(i, end=" ") # Separate by spaces and not by newlines
        
print("") # Add a newline in the end