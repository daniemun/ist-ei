#!/usr/bin/env python3

from math import ceil

min_number = int(input("Número inicial: "))
max_number = int(input("Número final: "))

pares_counter = 0

if min_number % 2 == 0: pares_counter += 1

pares_counter += ceil((max_number - min_number) / 2)

print(f"Quantidade de números pares entre {min_number} e {max_number}: {pares_counter}")