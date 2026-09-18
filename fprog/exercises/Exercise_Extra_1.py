#!/usr/bin/python3

while True:
    try:
        # Get input from user
        x = float(input("x = "))
        y = float(input("y = "))
        break
    except ValueError:
        print("Invalid number")

result = (x + 3 * y) * (x - y)
print(f"O valor de (x + 3 * y) * (x - y) = {result}")