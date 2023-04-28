import pytest
from random import randint
from ..sum_of_primes import is_prime, get_primes, get_sums_of_primes


@pytest.fixture
def prime_numbers():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


@pytest.fixture
def non_prime_numbers():
    return [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35]


@pytest.fixture
def negative_integers():
    return [-1, -8, -15]


@pytest.fixture
def non_integers():
    return [-10.2, -5.48, 25.39, "hello", "world"]


@pytest.fixture
def n_primes_dict():
    return {
        0: [],
        1: [],
        2: [2],
        3: [2, 3],
        4: [2, 3],
        5: [2, 3, 5],
        6: [2, 3, 5],
        7: [2, 3, 5, 7],
        8: [2, 3, 5, 7],
        9: [2, 3, 5, 7],
        10: [2, 3, 5, 7]
    }

@pytest.fixture
def sums_of_primes_dict():
    return {
        0: [0],
        1: [0, 0],
        2: [0, 0, 2],
        3: [0, 0, 2, 5],
        4: [0, 0, 2, 5, 5],
        5: [0, 0, 2, 5, 5, 10],
        6: [0, 0, 2, 5, 5, 10, 10],
        7: [0, 0, 2, 5, 5, 10, 10, 17],
        8: [0, 0, 2, 5, 5, 10, 10, 17, 17],
        9: [0, 0, 2, 5, 5, 10, 10, 17, 17, 17],
        10: [0, 0, 2, 5, 5, 10, 10, 17, 17, 17, 17]
    }


class TestIsPrime:

    def test_is_prime_valid_prime_numbers(self, prime_numbers):
        for num in prime_numbers:
            assert is_prime(num)

    def test_is_prime_valid_non_prime_numbers(self, non_prime_numbers):
        for num in non_prime_numbers:
            assert not is_prime(num)

    def test_is_prime_negative_integers(self, negative_integers):
        for num in negative_integers:
            assert not is_prime(num)

    def test_is_prime_non_integers(self, non_integers):
        for value in non_integers:
            with pytest.raises(TypeError):
                is_prime(value)


class TestGetPrimes:
    def test_get_primes_positive_integer_n(self, n_primes_dict):
        for n, expected_primes in n_primes_dict.items():
            primes = get_primes(n)
            assert isinstance(primes, list)
            assert primes == expected_primes

    def test_get_primes_negative_integer_n(self):
        negative_integer = -randint(1, 1000)
        primes = get_primes(negative_integer)
        assert isinstance(primes, list)
        assert len(primes) == 0

    def test_get_primes_invalid_input(self, non_integers):
        for value in non_integers:
            with pytest.raises(TypeError):
                get_primes(value)


class TestGetSumsOfPrimes:
    def test_get_sums_of_primes_valid_input(self, sums_of_primes_dict):
        for n, expected_sums_of_primes in sums_of_primes_dict.items():
            sums_of_primes = get_sums_of_primes(n)
            assert isinstance(sums_of_primes, list)
            assert sums_of_primes == expected_sums_of_primes

    def test_get_sums_of_primes_negative_integer_input(self, negative_integers):
        for value in negative_integers:
            with pytest.raises(ValueError):
                get_sums_of_primes(value)

    def test_get_sums_of_primes_non_integer_input(self, non_integers):
        for value in non_integers:
            with pytest.raises(TypeError):
                get_sums_of_primes(value)