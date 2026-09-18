#!/usr/bin/python3

while True:
    try:
        # Get input from user
        distance_kms = float(input("Distância (km) = "))
        time_mins = float(input("Tempo para percorrer (min.) = "))
        break
    except ValueError:
        print("Invalid number")
        
avg_velocity = distance_kms / (time_mins / 60)

print(f"Velocity: {avg_velocity:.1f} km/h")