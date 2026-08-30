"""
    Author: Leonardo Marques - 29/08/2026
    
    Exercise 2: Number as Text (★★✩✩✩)

    Write function number_as_text(n) which, for a given positive number, converts the
    respective digits into corresponding text.
    Start with the following fragment for the last digit of a number:

    def number_as_text(n):
        remainder = n % 10
        value_to_text = ""
        if remainder == 0:
            value_to_text = "ZERO"
        if remainder == 1:
            value_to_text = "ONE"
        # ...
        return value_to_text
    
    Examples

    | Input |        Result                   |
    |   7   |     “SEVEN”                     |
    |   42  |     “FOUR TWO”                  |
    | 24680 |     “TWO FOUR SIX EIGHT ZERO”   |
    | 13579 |     “ONE THREE FIVE SEVEN NINE” |
"""


def number_as_text(n) -> str:
    number_written = {
        "1" : "ONE",
        "2" : "TWO",
        "3" : "THREE",
        "4" : "FOUR",
        "5" : "FIVE",
        "6" : "SIX",
        "7" : "SEVEN",
        "8" : "EIGHT",
        "9" : "NINE",
        "0" : "ZERO"
    }

    return f"\"{" ".join([number_written[number] for number in str(n)])}\""


assert number_as_text(7) == f"\"SEVEN\""
assert number_as_text(42) == f"\"FOUR TWO\""
assert number_as_text(24680) == f"\"TWO FOUR SIX EIGHT ZERO\""
assert number_as_text(13579) == f"\"ONE THREE FIVE SEVEN NINE\""
