#!/usr/bin/env python3

from math import sqrt

#  x = ( -b +- sqrt(b**2 - 4ac) ) / 2a
def get_roots_quadratic_formula(a:int, b:int, c:int):

    if (a == 0) or (b**2 - 4*a*c < 0):
        return (float("NaN"), float("NaN"))
        
    x_sqrt = sqrt(b**2 - 4*a*c)
    plus_x = ( -b + x_sqrt ) / 2*a
    minus_x = ( -b - x_sqrt ) / 2*a
    
    return (minus_x, plus_x)
    
a_num = int(input("A: "))
b_num = int(input("B: "))
c_num = int(input("C: "))
    
print(f"The two roots are {get_roots_quadratic_formula(a_num, b_num, c_num)}")