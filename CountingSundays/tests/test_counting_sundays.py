import pytest

from ..counting_sundays import number_of_sundays_on_the_first_day_of_month

number_of_sundays_test_data = [
    [(1600, 1, 1), (1999, 12, 31), 688],
    [(1900, 1, 1), (1910, 1, 1), 18],
    [(2000, 1, 1), (2020, 1, 1), 35],
]


def explicit_test_ids(testcase):
    return str(testcase)


class TestNumberOfSundays:
    @pytest.mark.parametrize(
        "start_date, end_date, expected_result",
        number_of_sundays_test_data,
        ids=explicit_test_ids,
    )
    def test_valid_inputs_against_expected_outputs(
        self, start_date, end_date, expected_result
    ):
        start_year, start_month, start_day = [int(item) for item in start_date]
        end_year, end_month, end_day = [int(item) for item in end_date]

        calculated_sundays_on_the_first_day_of_month = (
            number_of_sundays_on_the_first_day_of_month(
                start_year, start_month, start_day, end_year, end_month, end_day
            )
        )
        assert calculated_sundays_on_the_first_day_of_month == expected_result

    def test_invalid_input_end_year_too_large(self):
        start_year = 10**16 + 1000 - 1
        start_month = 1
        start_day = 1
        end_year = 10**16 + 1000 + 1
        end_month = 1
        end_day = 1
        with pytest.raises(ValueError) as exc_info:
            number_of_sundays_on_the_first_day_of_month(
                start_year, start_month, start_day, end_year, end_month, end_day
            )
            expected = "End year can not be greater than"
            assert expected in str(exc_info)

    def test_invalid_start_year_too_large(self):
        start_year = 10**16 + 1000 + 1
        start_month = 1
        start_day = 1
        end_year = 10**16 + 1000 + 2
        end_month = 1
        end_day = 1

        with pytest.raises(ValueError) as exc_info:
            number_of_sundays_on_the_first_day_of_month(
                start_year, start_month, start_day, end_year, end_month, end_day
            )
            expected = "Start year can not be greater than"
            assert expected in str(exc_info)

    def test_start_date_greater_than_end_date(self):
        start_year = 2000
        start_month = 1
        start_day = 1
        end_year = start_year
        end_month = start_month
        end_day = start_day - 1

        with pytest.raises(ValueError) as exc_info:
            number_of_sundays_on_the_first_day_of_month(
                start_year, start_month, start_day, end_year, end_month, end_day
            )

            expected = "Start date can not be greater than end date."
            assert expected in str(exc_info)
