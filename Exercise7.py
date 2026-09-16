#!/usr/bin/env python

def encode_message(message: str, password: int) -> str:
    return ""
    
def decode_message(message: str, password: int) -> str:
    return ""

# Get input from user
message = input("Enter your message: ")

password = input("Enter the password (natural number): ")

# Validate n_many
if not password.isdigit():
    raise ValueError("Invalid password.")
    
password = int(password)
    
user_action = input("What do you want to do (ENC or DEC): ")

if user_action.lower() == "enc":
    encode_message(message, password)
    
elif user_action.lower() == "dec":
    decode_message(message, password)
    
else:
    raise ValueError("Invalid command.")