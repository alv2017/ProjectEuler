from math import sqrt

NMAX = 10**6


def is_prime(n):
    """
    :param n: an integer number N
    :return: True if N is prime, else False
    """
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(n: int) -> list:
    """
    :param n: integer N
    :return: list of prime numbers that are smaller than N
    """
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n < 0:
        return []
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def get_sums_of_primes(n: int) -> list:
    """
    :param n: positive integer N <= 10**6
    :return: list of sums of primes that are less or equal to N,
    the sum of primes that are less or equal to N has an index N.
    """
    if not isinstance(n, int):
        raise TypeError("N must be an integer")
    if n < 0:
        raise ValueError("N must be a positive.")
    if n > NMAX:
        raise ValueError(f"N can not exceed {NMAX}")
    primes_sum = 0
    if n == 0:
        return [0]
    if n == 1:
        return [0, 0]
    sums_of_primes = [0, 0]
    for i in range(2, n + 1):
        if is_prime(i):
            primes_sum += i
        sums_of_primes.append(primes_sum)
    return sums_of_primes


if __name__ == "__main__":
    # Looks weird, but solves HR problem :-)
    sum_of_primes = get_sums_of_primes(NMAX)
    for item in [5, 10, 100, 1000]:
        print(f"n = {item}, Sum Of Primes = {sum_of_primes[item]}")
