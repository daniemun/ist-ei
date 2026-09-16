#!/usr/bin/python3

# https://stackoverflow.com/a/19242084
from collections import defaultdict
from math import sqrt

max_number_limit = 1000

def is_prime(number: int) -> bool:
    for i in range(2, int(sqrt(number)) + 1): # 2 to square root + 1
        if number % i == 0: return False
        
    return True

def get_next_prime(number: int):
    prime_number = number + 1
    
    while not is_prime(prime_number): 
        prime_number += 1 # Keep adding until it's prime (crude method I know)
    
    return prime_number

# Python is dumb and normal dictionaries don't support integer keys
primes_dict = defaultdict(int) # {base, exponent}

# Get input from user
number = input(f"Enter number from 0 to {max_number_limit}: ")

# Validate number_start
if not number.isdigit():
    raise ValueError("Invalid number.")
    
number = int(number)

if number > max_number_limit:
    raise ValueError("Invalid number.")

prime_factor = 2

while number > 1:
    if number % prime_factor == 0:
        primes_dict[prime_factor] += 1 # Add +1 exponent to base
        number /= prime_factor
    else:
        prime_factor = get_next_prime(prime_factor)

# Output values
for key, value in primes_dict.items():
    print(f"{key} ** {value}")