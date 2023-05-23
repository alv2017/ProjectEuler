from .utils import GRAND_UNITS, NUMBERS


def number_to_string(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("Invalid type: input value must be an integer.")
    if n < 0:
        raise ValueError("Value Error: input value must be non-negative integer")
    if n > 10**15 - 1:
        raise ValueError("Value Error: input value is too big.")
    if n == 0:
        return "Zero"
    number_as_string = ""
    counter = 0
    while n:
        residual = n % 1000
        hundreds = residual // 100
        number = residual % 100
        unit = GRAND_UNITS[1000**counter]
        n = n // 1000
        counter += 1

        if not residual:
            continue

        number_as_string = unit + " " + number_as_string
        if number:
            number_as_string = NUMBERS[number] + " " + number_as_string
        if hundreds:
            number_as_string = NUMBERS[hundreds] + " Hundred " + number_as_string
    return number_as_string.strip()
