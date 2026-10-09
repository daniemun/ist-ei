#!/usr/bin/env python3

user_input = int(input("Number: "))

pot2 = 1
log2 = -1

while pot2 <= user_input:
    pot2 *= 2
    log2 += 1
    
print(f"log2({user_input}) = {log2}")