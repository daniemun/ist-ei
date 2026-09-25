#!/usr/bin/env python3

from math import sqrt

def is_prime(x: int) -> bool:
    if x <= 1: return False
    
    counter = 2

    while counter < int(sqrt(x)) + 1:
        if x % counter == 0:
            return False
            
        counter += 1
            
    return True
            

number = int(input("Número: "))

if is_prime(number):
    print(f"{number} é primo!")
else:
    print(f"{number} não é primo!")