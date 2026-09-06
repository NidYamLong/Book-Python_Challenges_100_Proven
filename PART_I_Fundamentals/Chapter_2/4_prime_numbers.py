"""
    Author: Leonardo Marques - 06/09/2026

    Exercise 4: Prime Numbers (★★✩✩✩)

    Write function calc_primes_up_to(max_value) to compute all prime numbers up
    to a given value. As a reminder, a prime number is a natural number greater than 1
    and exclusively divisible by itself and by 1. To compute a prime number, the Sieve of
    Eratosthenes was described before.
    
    Examples

    Check your algorithm with the following values:

    | Input |         Result                                            |
    |  15   | [2, 3, 5, 7, 11, 13]                                      |
    |  25   | [2, 3, 5, 7, 11, 13, 17, 19, 23]                          |
    |  50   | [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]  |

    link: https://nickymeuleman.netlify.app/blog/sieve-of-eratosthenes/
"""


from math import sqrt


def calc_primes_up_to(max_value) -> []:

    numbers = [True for _ in range(max_value + 1)]
    primes = []

    for index in range(2, int(sqrt(max_value)) + 1):
        if numbers[index]:
            for n in range(index * index, max_value + 1, index):
                numbers[n] = False

    for number in range(2, max_value + 1):
        if numbers[number]:
            primes.append(number)

    return primes



assert calc_primes_up_to(15) == [2, 3, 5, 7, 11, 13]
assert calc_primes_up_to(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
assert calc_primes_up_to(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]