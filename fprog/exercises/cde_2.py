#!/usr/bin/env python3

max_number = int(input("Número limite: "))
div_number = int(input("Número divisível: "))

counter = 0
quantidade_divisiveis = 0

while counter <= max_number:
    if counter % div_number == 0:
        print(f"{counter} é divisível por {div_number}")
        quantidade_divisiveis += 1
        
    counter += 1
    
print(f"Existem {quantidade_divisiveis} números divisíveis por {div_number} até {max_number}")