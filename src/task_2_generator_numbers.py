import re
from typing import Callable

def generator_numbers(string: str):
    string = string.strip()
    while string:
        [substr, string] = string.split(" ", 1)\
            if " " in string\
            else [string, ""]
        substr = substr.strip()
        if re.match(r"^\d+\.\d+$", substr):
            yield float(substr)

def sum_profit(text: str, func: Callable):
    sum = 0
    for n in func(text):
        sum += n
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")