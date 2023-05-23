import pytest

from ..number_to_words import number_to_string


@pytest.fixture
def non_integer_input_values():
    return [
        {"input_value": "some string"},
        {"input_value": "One Hundred"},
        {"input_value": 2.35},
        {"input_value": -10.25},
    ]


@pytest.fixture
def negative_integers():
    return [
        {"input_value": -1},
        {"input_value": -2},
        {"input_value": -100},
    ]


@pytest.fixture
def too_large_numbers():
    return [
        {"input_value": 10**15},
        {"input_value": 10**15 + 1},
        {"input_value": 10**15 + 1000},
        {"input_value": 10**16},
        {"input_value": 10**20},
    ]


@pytest.fixture
def valid_inputs():
    return [
        {"input_value": 1, "expected_output": "One"},
        {"input_value": 5, "expected_output": "Five"},
        {"input_value": 10, "expected_output": "Ten"},
        {"input_value": 12, "expected_output": "Twelve"},
        {"input_value": 52, "expected_output": "Fifty Two"},
        {"input_value": 100, "expected_output": "One Hundred"},
        {"input_value": 105, "expected_output": "One Hundred Five"},
        {"input_value": 199, "expected_output": "One Hundred Ninety Nine"},
        {"input_value": 500, "expected_output": "Five Hundred"},
        {"input_value": 511, "expected_output": "Five Hundred Eleven"},
        {"input_value": 1000, "expected_output": "One Thousand"},
        {
            "input_value": 1783,
            "expected_output": "One Thousand Seven Hundred Eighty Three",
        },
        {"input_value": 10000, "expected_output": "Ten Thousand"},
        {"input_value": 100000, "expected_output": "One Hundred Thousand"},
        {"input_value": 1000000, "expected_output": "One Million"},
        {
            "input_value": 110235680,
            "expected_output": "One Hundred Ten Million Two Hundred Thirty Five Thousand Six Hundred Eighty",
        },
    ]


class TestNumberToString:
    def test_input_value_zero(self):
        input_value = 0
        expected_output = "Zero"
        actual_output = number_to_string(input_value)
        assert actual_output == expected_output

    def test_valid_inputs(self, valid_inputs):
        for item in valid_inputs:
            input_value = item["input_value"]
            expected_output = item["expected_output"]
            actual_output = number_to_string(input_value)
            assert actual_output == expected_output

    def test_invalid_input_non_integers(self, non_integer_input_values):
        for item in non_integer_input_values:
            input_value = item["input_value"]
            with pytest.raises(TypeError) as exc_info:
                number_to_string(input_value)
            expected_error_message = "value must be an integer"
            assert expected_error_message in str(exc_info)

    def test_invalid_input_negative_integers(self, negative_integers):
        for item in negative_integers:
            input_value = item["input_value"]
            with pytest.raises(ValueError) as exc_info:
                number_to_string(input_value)
            expected_error_message = "input value must be non-negative integer"
            assert expected_error_message in str(exc_info)

    def test_invalid_input_too_large_numbers(self, too_large_numbers):
        for item in too_large_numbers:
            input_value = item["input_value"]
            with pytest.raises(ValueError) as exc_info:
                number_to_string(input_value)
            expected_error_message = "input value is too big"
            assert expected_error_message in str(exc_info)
