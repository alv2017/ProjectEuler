import pytest

from ..power_digit_sum import sum_of_digits


@pytest.fixture
def valid_positive_integers():
    return [
        {"n": 3, "expected_result": 8},
        {"n": 4, "expected_result": 7},
        {"n": 7, "expected_result": 11},
    ]


@pytest.fixture
def invalid_positive_integers():
    return [1001, 4000, 1500]


@pytest.fixture
def non_integers():
    return [2.3, "hello", "10"]


@pytest.fixture
def negative_integers():
    return [-100, -1, -52]


class TestPowerDigitSum:
    def test_power_digit_sum_valid_input(self, valid_positive_integers):
        for item in valid_positive_integers:
            n = item["n"]
            result = sum_of_digits(n)
            expected_result = item["expected_result"]
            assert result == expected_result

    def test_power_digit_sum_invalid_integer_input(self, invalid_positive_integers):
        for item in invalid_positive_integers:
            with pytest.raises(ValueError):
                sum_of_digits(item)

    def test_power_digit_sum_non_integer_input(self, non_integers):
        for item in non_integers:
            with pytest.raises(TypeError):
                sum_of_digits(item)

    def test_power_digit_sum_negative_integer_input(self, negative_integers):
        for item in negative_integers:
            with pytest.raises(ValueError):
                sum_of_digits(item)
