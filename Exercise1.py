#!/usr/bin/env python

# Get user input data
username = input("Enter your name: ")
country = input("Enter your country: ")

# Extract first name from full username
firstname = username.split(" ")[0]

# Print output
print(f"Nice to meet you, {firstname}! Welcome to {country}.")