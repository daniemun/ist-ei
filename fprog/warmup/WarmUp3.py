#!/usr/bin/python3

while True:
    try:
        number = int(input("Number = "))
        break
    except ValueError:
        print("Invalid number!")

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")