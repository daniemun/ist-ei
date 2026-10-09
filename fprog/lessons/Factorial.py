#!/usr/bin/env python3

import sys

sys.set_int_max_str_digits(0x7FFFFFFF)

def factorial(x:int) -> int:
    f = 1

    for i in range(1, x + 1):
        f *= i
    
    return f
    
limit_number = int(input("Give me a number: "))

for i in range(1, limit_number + 1):
    print(f"{i}! = {factorial(i)}")