#!/usr/bin/env python3

def get_input() -> int:
    n:int = 0
    while True:
        try:
            n = int(input("n: "))
            if n >= 0:
                break
        except ValueError:
            print("Invalid number")
    
    return n

def fibo(x: int) -> list[int]:
    ret_list: list[int] = []
    a, b = 0, 1
    for _ in range(x):
        ret_list.append(a)
        a, b = a + b, a
        
    return ret_list

def main():
    n = get_input()
    
    for i in fibo(n):
        print(i)
        
if __name__ == "__main__":
    main()