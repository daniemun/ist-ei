#!/usr/bin/python3

while True:
    try:
        numberA = int(input("Number A = "))
        numberB = int(input("Number B = "))
        break
    except ValueError:
        print("Invalid number!")

if numberA == numberB:
    print("A = B")
else:
    print("A != B")