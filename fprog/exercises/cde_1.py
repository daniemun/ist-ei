#!/usr/bin/env python3

max_number = int(input("Número limite: "))

soma = 0
counter = 0


while counter < max_number:
    soma += counter * counter
    counter += 1
    
print(f"Soma: {soma}")