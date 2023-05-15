from math import comb


def lattice_routes(m: int, n: int) -> int:
    """Calculates the number of routes from upper-left to bottom-right corner in the m x n lattice
    :param m: int, grid height
    :param n: int, grid width
    :return: int, number of routes through the m x n grid
    """
    if m <= 0:
        raise ValueError("Invalid Lattice Size: Grid height must be positive.")
    if m > 500:
        raise ValueError("Invalid Lattice Size: Grid height must not exceed 500.")
    if n <= 0:
        raise ValueError("Invalid Lattice Size: Grid width must be positive.")
    if n > 500:
        raise ValueError("Invalid Lattice Size: Grid width must not exceed 500.")
    return comb(m + n, m)


if __name__ == "__main__":
    # Hacker Rank Solution Imitation
    modulo_coefficient = 10**9 + 7
    input_data = [{"m": 2, "n": 2}, {"m": 3, "n": 2}]
    for tc in input_data:
        m = tc["m"]
        n = tc["n"]
        result = lattice_routes(m, n)
        print(result % modulo_coefficient)
