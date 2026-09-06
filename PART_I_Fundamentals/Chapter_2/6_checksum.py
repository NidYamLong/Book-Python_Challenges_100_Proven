"""
    Author: Leonardo Marques - 06/09/2026

    Exercise 6: Checksum (★★✩✩✩)

    Create function calc_checksum(digits) that performs the following position-based
    calculation for the checksum of a number of any length given as a string, with the n digits
    modeled as z1 to zn:

    z1 z2 z3 ... zn -> (1 * z1 + 2 * z2 + 3 * z3 ... n * zn ) % 10
   
    Examples

    |   Input      |            Sum                            |      Result      |
    | “11111”      |      1 + 2 + 3 + 4 + 5 = 15               |      15 % 10 = 5 |
    | “87654321”   | 8 + 14 + 18 + 20 + 20 + 18 + 14 + 8 = 120 |     120 % 10 = 0 |
"""


def calc_checksum(digit)-> int:
    sum_total = 0

    for index,c in enumerate(digit):
        sum_total += int(c) * (index+1)

    return sum_total % 10


assert calc_checksum("11111") == 5
assert calc_checksum("87654321") == 0