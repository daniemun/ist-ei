#!/usr/bin/python3

while True:
    try:
        # Get input from user
        n_seconds = float(input("Num. of seconds = "))
        break
    except ValueError:
        print("Invalid number")

n_days = n_seconds // 60 // 60 // 24;
n_seconds -= n_days * 60 * 60 * 24;

n_hours = n_seconds // 60 // 60;
n_seconds -= n_hours * 60 * 60;

n_minutes = n_seconds // 60;
n_seconds -= n_minutes * 60;

print(f"{n_days:.0f}d {n_hours:.0f}h {n_minutes:.0f}m {n_seconds:.0f}s")