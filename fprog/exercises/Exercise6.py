#!/usr/bin/python3

bananas = 0
loquats = 0
oranges = 0
apples = 0

counting_ended = False

print("[Video camera input]")
while not counting_ended:
    video_camera_input = input("> ")
    
    # For every letter in the input
    for letter in video_camera_input:
    
        if letter == 'B':
            bananas += 1
        elif letter == 'N':
            loquats += 1
        elif letter == 'L':
            oranges += 1
        elif letter == 'M':
            apples += 1
        
        elif letter == 'X':
            counting_ended = True # End video camera input streaming
            break # We won't read anything after 'X'

# Output fruits
print(f"Bananas = {bananas}\nOranges = {oranges}\nLoquats = {loquats}\nApples = {apples}")