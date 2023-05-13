import pytest

from ..collatz_sequence import CollatzSequence


@pytest.fixture
def known_collatz_sequences():
    return {
        1: [1],
        2: [2, 1],
        3: [3, 10, 5, 16, 8, 4, 2, 1],
        9: [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
        23: [23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1],
        100: [
            100,
            50,
            25,
            76,
            38,
            19,
            58,
            29,
            88,
            44,
            22,
            11,
            34,
            17,
            52,
            26,
            13,
            40,
            20,
            10,
            5,
            16,
            8,
            4,
            2,
            1,
        ],
    }


@pytest.fixture
def known_collatz_sequence_lengths(known_collatz_sequences):
    data = {}
    for k, v in known_collatz_sequences.items():
        data[k] = len(v)
    return data


@pytest.fixture
def known_collatz_max_length_items():
    return {
        1: 1,
        2: 2,
        3: 3,
        4: 3,
        5: 3,
        6: 6,
        7: 7,
        8: 7,
        9: 9,
        10: 9,
        11: 9,
        12: 9,
        13: 9,
        14: 9,
        15: 9,
        16: 9,
        17: 9,
        18: 18,
        19: 19,
        20: 19,
    }


class TestCollatzSequence:
    def test_collatz_sequence(self, known_collatz_sequences):
        for start, sequence in known_collatz_sequences.items():
            expected_sequence = sequence
            calculated_sequence = CollatzSequence.collatz_sequence(start)
            assert calculated_sequence == expected_sequence

    def test_sequence_length(self, known_collatz_sequence_lengths):
        max_size = max(known_collatz_sequence_lengths.keys())
        cs = CollatzSequence(max_size)

        for start, length in known_collatz_sequence_lengths.items():
            expected_length = length
            calculated_length = cs.sequence_length(start)
            assert calculated_length == expected_length

    def test_get_max_length_item(self, known_collatz_max_length_items):
        max_size = max(known_collatz_max_length_items.keys())
        cs = CollatzSequence(max_size)
        for start, max_sequence_item in known_collatz_max_length_items.items():
            expected_max_sequence_element = max_sequence_item
            calculated_max_sequence_element = cs.get_max_length_item(start)
            assert calculated_max_sequence_element == expected_max_sequence_element

    def test_get_max_length_item_parameter_raises_exception_when_max_size_exceeded(
        self,
    ):
        max_size = 100
        cs = CollatzSequence(max_size)
        with pytest.raises(ValueError):
            cs.get_max_length_item(max_size + 1)
