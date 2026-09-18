#!/usr/bin/python3

while True:
    try:
        # Get input from user
        n_passangers = float(input("Num. of passangers = "))
        plane_consumption = float(input("Plane's consumption (miles / gallon) = "))
        break
    except ValueError:
        print("Invalid number")

miles_per_gallon = plane_consumption / n_passangers;
gallon_per_miles = 1 / miles_per_gallon;

print(f"Plane's gallon / miles: {gallon_per_miles:.2f}")