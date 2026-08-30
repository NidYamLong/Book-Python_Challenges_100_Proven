"""
    Author: Leonardo Marques - 29/08/2026

    Exercise 1a: Basic Arithmetic Operations (★✩✩✩✩)

    Write function calc(m, n) that multiplies two variables m and n of type int, then
    divides the product by two, and outputs the remainder with respect to division by 7.

    Examples
        | m | n | m*n | m * n//2 | Result((n * m // 2) % 7)|
        | 6 | 7 |  42 |   21     |         0               |
        | 5 | 5 |  25 |   12     |         5               |

    A short reminder: With an i
"""

def calc(m, n) -> int:
    return ((n * m // 2) % 7)


assert calc(6, 7) == 0
assert calc(5, 5) == 5
assert calc(10, 9) == 3