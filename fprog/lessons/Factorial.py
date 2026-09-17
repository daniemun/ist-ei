#!/usr/bin/python3

# Read input number
n = int(input("Number: "))

f = 1

for i in range(1, n+1):
    f = f * i

print("the factorial of", n, "is", f)