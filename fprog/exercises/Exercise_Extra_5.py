#!/usr/bin/python3

while True:
    try:
        # Get input from user
        n_seconds = float(input("Num. of seconds = "))
        break
    except ValueError:
        print("Invalid number")

n_days = n_seconds / 60 / 60 / 24;

print(f"Days: {n_days:.2f}")