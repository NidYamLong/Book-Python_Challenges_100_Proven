"""
    Author: Leonardo Marques - 06/09/2026

    Exercise 5: Prime Number Pairs (★★✩✩✩)

    Compute all pairs of prime numbers with a distance of 2 (twin), 4 (cousin), and 6 (sexy)
    up to an upper bound for n. For twins then the following is true:

    is_Prime(n) && is_Prime(n + 2)

    Examples

    The following results are expected for limit 50:

    | Type     |                   Result                                                         |
    | twin     | {3: 5, 5: 7, 11: 13, 17: 19, 29: 31, 41: 43}                                     |
    | cousin   | {3: 7, 7: 11, 13: 17, 19: 23, 37: 41, 43: 47}                                    |
    | sexy     | {5: 11, 7: 13, 11: 17, 13: 19, 17: 23, 23: 29, 31: 37, 37: 43, 41: 47, 47: 53}   |
"""


from math import sqrt


def generate_numbers_prime(max_value) -> []:
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


def is_prime(value, distance="twin") -> {}:
    d = 0

    match distance:
        case "cousin":
            d = 4
        case "sexy":
            d = 6
        case _:
            d = 2

    list_numbers_prime = generate_numbers_prime(value + d)
    dict_prime = {}

    for number in list_numbers_prime:
        if(number + d in list_numbers_prime):
            dict_prime[number] = number + d

    return dict_prime


assert is_prime(50) == {3: 5, 5: 7, 11: 13, 17: 19, 29: 31, 41: 43} 
assert is_prime(50, "cousin") == {3: 7, 7: 11, 13: 17, 19: 23, 37: 41, 43: 47}
assert is_prime(50, "sexy") == {5: 11, 7: 13, 11: 17, 13: 19, 17: 23, 23: 29, 31: 37, 37: 43, 41: 47, 47: 53}