#!/usr/bin/env python3

from random import randint
from math import log2

def main():
    while True:
        try:
            limit_secret_value = int(input("Escreva um número > 4: "))
            if limit_secret_value > 4:
                break
            
        except ValueError:
            continue
        
    secret_number = randint(1, limit_secret_value)
    
    num_tentativas = (int(log2(secret_number))) + 1
    adivinhou = False
    
    print(f"Tens {num_tentativas} tentativas para adivinhar o número secreto entre 0 e {limit_secret_value}!")
    
    while not adivinhou and num_tentativas > 0:
        try:
            user_guess = int(input(f"{num_tentativas} tentativas: "))
        except ValueError:
            continue
            
        if user_guess < secret_number:
            print("Maior!")
            num_tentativas -= 1
            
        elif user_guess > secret_number:
            print("Menor!")
            num_tentativas -= 1
            
        else:
            adivinhou = True
        
    if adivinhou:
        print("Ganhaste, parabéns!")
    else:
        print("Dedica-te à pesca.")
    
if __name__ == "__main__":
    main()