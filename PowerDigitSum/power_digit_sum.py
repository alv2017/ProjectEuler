def sum_of_digits(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be positive")
    if n > 1000:
        raise ValueError("n must be smaller that 1000")
    s = 0
    num = 2**n
    while num // 10:
        s += num % 10
        num = num // 10
    s += num % 10
    return s
