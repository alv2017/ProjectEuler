import re

pattern = re.compile(r"[1-9]\d*")


def input_validation(num, k: int):
    # Type Validation
    if not isinstance(k, int):
        raise TypeError("Length of sequence must be an integer")
    if not isinstance(num, str):
        raise TypeError("Number string: must be a string")

    # Value Validation
    if not re.fullmatch(pattern, num):
        raise ValueError(
            "Integer number string: represents an integer and can contain digits only"
        )
    # Value Validation
    if k < 1 or k > 7:
        raise ValueError("Length of sequence must satisfy the condition: 1 <= k <= 7")
    # Number length validation
    if len(num) < k:
        raise ValueError(
            "The number of digits in the number string can not be smaller than the length of sequence."
        )


def largest_series_product(num: str, k: int) -> int:
    max_product = 0
    num_length = len(num)

    for idx in range(num_length - k + 1):
        result = 1
        for item in num[idx : idx + k]:
            result *= int(item)
        max_product = max(max_product, result)
    return max_product


if __name__ == "__main__":
    n = "1234567890"
    k = 3
    expected_result = 7 * 8 * 9
    input_validation(n, k)
    result = largest_series_product(n, k)
    assert result == expected_result
