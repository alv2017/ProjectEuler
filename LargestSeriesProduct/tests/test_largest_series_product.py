import csv
import os
import pathlib

import pytest

from ..largest_series_product import input_validation, largest_series_product

TEST_DIR = pathlib.Path(__file__).parent.resolve()
TEST_FILE = os.path.join(TEST_DIR, "test_data.csv")


@pytest.fixture
def test_data():
    data = []
    with open(TEST_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["N"] = str(row["N"])
            row["K"] = int(row["K"])
            row["LSP"] = int(row["LSP"])
            data.append(row)
    return data


@pytest.fixture()
def valid_input_data():
    data = [
        {"n": "123456789", "k": 1},
        {"n": "123456789", "k": 2},
        {"n": "123456789", "k": 5},
        {"n": "123456789", "k": 7},
    ]
    return data


@pytest.fixture()
def invalid_input_data():
    data = [
        {
            "n": "123456789",
            "k": "some string",
            "error_type": TypeError,
            "error_msg": "Length of sequence must be an integer",
        },
        {
            "n": "123456789",
            "k": "1",
            "error_type": TypeError,
            "error_msg": "Length of sequence must be an integer",
        },
        {
            "n": 123456789,
            "k": 1,
            "error_type": TypeError,
            "error_msg": "Number string: must be a string",
        },
        {
            "n": "Hello, World!",
            "k": 1,
            "error_type": ValueError,
            "error_msg": "Integer number string: represents an integer and can contain digits only",
        },
        {
            "n": "123.23",
            "k": 1,
            "error_type": ValueError,
            "error_msg": "Integer number string: represents an integer and can contain digits only",
        },
        {
            "n": "1234567",
            "k": 0,
            "error_type": ValueError,
            "error_msg": "Length of sequence must satisfy the condition: 1 <= k <= 7",
        },
        {
            "n": "1234567",
            "k": 8,
            "error_type": ValueError,
            "error_msg": "Length of sequence must satisfy the condition: 1 <= k <= 7",
        },
        {
            "n": "12345",
            "k": 6,
            "error_type": ValueError,
            "error_msg": "The number of digits in the number string can not be smaller than the length of sequence.",
        },
        {
            "n": "12345",
            "k": 7,
            "error_type": ValueError,
            "error_msg": "The number of digits in the number string can not be smaller than the length of sequence.",
        },
    ]
    return data


class TestInputValidation:
    def test_valid_input(self, valid_input_data):
        for item in valid_input_data:
            n = item["n"]
            k = item["k"]
            assert input_validation(n, k) is None

    def test_invalid_input(self, invalid_input_data):
        for item in invalid_input_data:
            n = item["n"]
            k = item["k"]
            error_type = item["error_type"]
            error_msg = item["error_msg"]
            with pytest.raises(error_type) as exception_info:
                input_validation(n, k)
            assert error_msg in str(exception_info.value)


class TestLargestSeriesProduct:
    def test_largest_series_product_examples(self):
        k = 5
        num01 = "3675356291"
        num02 = "2709360626"
        expected_result01 = 3150
        expected_result02 = 0
        actual_result01 = largest_series_product(num01, k)
        actual_result02 = largest_series_product(num02, k)
        assert isinstance(actual_result01, int)
        assert isinstance(actual_result02, int)
        assert actual_result01 == expected_result01
        assert actual_result02 == expected_result02

    def test_largest_series_product_test_data(self, test_data):
        for item in test_data:
            num = item["N"]
            k = item["K"]
            expected_lsp = item["LSP"]
            actual_lsp = largest_series_product(num, k)
            assert isinstance(actual_lsp, int)
            assert expected_lsp == actual_lsp
