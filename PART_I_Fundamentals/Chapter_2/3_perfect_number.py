"""
    Author: Leonardo Marques - 29/08/2026

    Exercise 3: Perfect Numbers (★★✩✩✩)

    By definition, a natural number is called a perfect number if its value is equal to the sum
    of its real divisors. This is true, for example, for the numbers 6 and 28:

        1 + 2 + 3 = 6

        1 + 2 + 4 + 7 + 14 = 28

    Write function calc_perfect_numbers(max_exclusive) that calculates the perfect
    numbers up to a maximum value, say 10,000.

    Examples

    | Input    |      Result        |
    | 1000     |   [6, 28, 496]     |
    | 10000    | [6, 28, 496, 8128] |

    link formula -> https://mathworld.wolfram.com/PerfectNumber.html
"""


def isPrime(number) -> bool:
    if  number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

def calc_perfect_numbers(max_exclusive) -> []:
    perfect_numbers = []

    for i in range(max_exclusive):
        if isPrime(2 ** i - 1):
            number = 2 ** (i - 1) * (2 ** i - 1)

            if number < max_exclusive:
                perfect_numbers.append(number)

            else:
                break

    return perfect_numbers

assert calc_perfect_numbers(10) == [6]
assert calc_perfect_numbers(100) == [6, 28]
assert calc_perfect_numbers(1000) == [6, 28, 496]
assert calc_perfect_numbers(10000) == [6, 28, 496, 8128]