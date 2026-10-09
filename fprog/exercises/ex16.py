#!/usr/bin/env python3

def sumup(x: int) -> int:
    total_sum: int = 0
    for i in range(0, x + 1):
        total_sum += i
    return total_sum
    
def mulup(x: int) -> int:
    total_mul: int = 1
    for i in range(1, x + 1):
        total_mul *= i
    return total_mul
    
def main() -> None:
    program_running = True
    while program_running:
        try:
            command_input = input("Command: ")
            command = command_input.split(' ')
                
            if command[0].lower() == "quit":
                program_running = False
                continue
            
            if len(command) != 2:
                print("Usage: [SUM / MUL / QUIT] [int]")
                continue
            
            n_input = int(command[1])
            
            if command[0].lower() == "sum":
                print(f"Sum: {sumup(n_input)}")
            elif command[0].lower() == "mul":
                print(f"Mul: {mulup(n_input)}")
            else:
                print("Usage: [SUM / MUL / QUIT] [int]")
                continue
                
        except ValueError:
            print("Usage: [SUM / MUL / QUIT] [int]")
            
if __name__ == "__main__":
    main()