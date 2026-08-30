"""
    Author: Leonardo Marques - 29/08/2026
    
    Exercise 1b: Statistics (★★✩✩✩)

    Count as well as sum up the natural numbers that are divisible by 2 or 7 up to a given
    maximum value (exclusive) and output it to the console. Write function calc_sum_and_
    count_all_numbers_div_by_2_or_7(max_exclusive). Extend it so that it returns the
    two values instead of performing the console output.

    Examples

    | Maximum |       Divisible by 2   | Divisible by 7 | Result | CountSum |     
    |   3     |            2           |      -/-       |   1    |    2     |
    |   8     |        2, 4, 6         |       7        |   4    |    19    |
    |   15    | 2, 4, 6, 8, 10, 12, 14 |      7, 14     |   8    |    63    |
"""


def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive) -> int:
    set_divisible = {number for number in range(1, max_exclusive) if number % 2 == 0  or number % 7 == 0}

    return len(set_divisible), sum(set_divisible)


assert calc_sum_and_count_all_numbers_div_by_2_or_7(3) == (1, 2)
assert calc_sum_and_count_all_numbers_div_by_2_or_7(8) == (4, 19)
assert calc_sum_and_count_all_numbers_div_by_2_or_7(15) == (8, 63)