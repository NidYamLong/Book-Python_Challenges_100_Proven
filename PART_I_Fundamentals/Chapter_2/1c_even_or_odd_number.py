"""
    Author: Leonardo Marques - 29/08/2026
    
    Exercise 1c: Even or Odd Number (★✩✩✩✩)

    Create the functions is_even(n) and is_odd(n) that will check if the passed integer is
    even or odd, respectively.
"""

def is_even(n) -> bool:
    return n % 2 != 0

def is_odd(n) -> bool:
    return n % 2 == 0

assert is_even(3) == True
assert is_odd(2) == True
assert is_even(4) == False
assert is_odd(5) == False
assert is_even(39) == True
assert is_odd(25) == False