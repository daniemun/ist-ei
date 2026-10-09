#!/usr/bin/env python3

def fibonacci(x: int) -> list[int]:
    ret_list: list[int] = []
    a, b = 0, 1
    for _ in range(x):
        ret_list.append(a)
        a, b = a + b, a
        
    return ret_list

n = int(input("n: "))

for i in fibonacci(n):
    print(i)