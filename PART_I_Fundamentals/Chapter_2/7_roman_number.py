"""
    Author: Leonardo Marques - 20/09/2026

    Exercise 7: Roman Numbers (★★★★✩)

    Exercise 7a: Roman Numbers ➤ Decimal Numbers (★★★✩✩)
    Write function from_roman_number(roman_number) that computes the corresponding
    decimal number from a textually valid Roman number.4

    Exercise 7b: Decimal Numbers ➤ Roman Numbers (★★★★✩)
    Write function to_roman_number(value) that converts a decimal number to a (valid)
    Roman number.

    Examples

    | Arabic | Roman     |
    |  17    | “XVII”    |
    |  444   | “CDXLIV”  |
    |  1971  | “MCMLXXI” |
    |  2020  | “MMXX”    |
"""


def from_roman_number(roman_number) -> int:
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    stack = []
    number = 0
    
    for i in roman_number.upper():
        if i in numbers.keys():
            stack.append(numbers[i])
        else:
            raise("Invalid Roman symbol!!!")
    
    while(len(stack) != 0):
        value = stack.pop()
        
        if len(stack) >= 1:
            if stack[-1] < value:
                number += value - stack.pop()
            else:
                number += value
        else:
            number += value
                
            
    return number


def to_roman_number(roman_number) -> str:
    numbers = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    stack = []
    r = ""
    
    for index, i in enumerate(str(roman_number)[::-1]):
        stack.append(int(i) * (10**index))
        
    
    while(len(stack) != 0):
        value = stack.pop()
        
        if ("4" in str(value) or "9" in str(value)) and value < max(numbers):
            r += numbers[10**(len(str(value))-1)]
            r += numbers[value + 10**(len(str(value))-1)]
        
        elif value not in numbers.keys():
            n = value
            
            while(n != 0):
                max_value = 0
                
                for i in numbers.keys():
                    if i <= n:
                        max_value = i
                        
                    if i > n:
                        break
                
                
                r += numbers[max_value]
                n -= max_value
            
        else:
            r += numbers[value]
            
    return r


assert from_roman_number("XVII") == 17
assert from_roman_number("CDXLIV") == 444
assert from_roman_number("MCMLXXI") == 1971
assert from_roman_number("MMXX") == 2020


assert to_roman_number(397) == "CCCXCVII"
assert to_roman_number(15) == "XV"
assert to_roman_number(4444) == "MMMMCDXLIV"
assert to_roman_number(57) == "LVII"


assert from_roman_number(to_roman_number(87)) == 87
assert from_roman_number(to_roman_number(498)) == 498
assert from_roman_number(to_roman_number(1537)) == 1537
assert from_roman_number(to_roman_number(2485)) == 2485


assert to_roman_number(from_roman_number("XIV")) == "XIV"
assert to_roman_number(from_roman_number("XLVII")) == "XLVII"
assert to_roman_number(from_roman_number("LXXXIII")) == "LXXXIII"
assert to_roman_number(from_roman_number("CXXVI")) == "CXXVI"