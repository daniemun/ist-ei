#!/usr/bin/python3

# Get input from user
n_many = input("Enter the bigger number (n_many): ")

# Validate n_many
if not n_many.isdigit():
    raise ValueError("Invalid number.")

n_many = int(n_many)

result = 0

# From 0 to n_many, only sum odd number to the result
for i in range(n_many):
    if i % 2 != 0:
        result += i

# Output sum
print(f"Result: {result}")