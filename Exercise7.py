#!/usr/bin/env python

# Get alphabet (printable chars) length from last printable char - first printable char
alphabet_length = ord('~') - ord(' ')

# Encode message with integer password
def encode_message(message: str, password: int) -> str:
    encoded_message = ""
    
    for char in message:
        # ( n + K ) mod alphabet_length
        encoded_message += chr((ord(char) + password) % alphabet_length)
        
    return encoded_message

# Decode message with intger password
def decode_message(message: str, password: int) -> str:
    decoded_message = ""
    
    for char in message:
        # TODO: Can't "reverse engineer" the mod, might give wrong results
        decoded_message += chr(ord(char) - password);
    
    return decoded_message

# Get input from user
message = input("Enter your message: ")

if len(message) == 0:
    raise ValueError("Empty message.")

password = input("Enter the password (natural number): ")

# Validate password
if not password.isdigit():
    raise ValueError("Invalid password.")
    
password = int(password)
    
user_action = input("What do you want to do (ENC or DEC): ")

if user_action.lower() == "enc":
    result = encode_message(message, password)
    
elif user_action.lower() == "dec":
    result = decode_message(message, password)
    
else:
    raise ValueError("Invalid command.")
    
print(f"Output: {result}");