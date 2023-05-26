from datetime import date, timedelta


def number_of_sundays_on_the_first_day_of_month(
    y1: int, m1: int, d1: int, y2: int, m2: int, d2: int
):
    # Input validation
    if y1 > 10**16 + 1000 or y2 > 10**16 + 1:
        raise ValueError("Start year can not be greater than 10**13 + 1000")

    if y2 > 10**16 + 1:
        raise ValueError("End year can not be greater than 10**13 + 1000")

    actual_start_date = date(y1, m1, d1)
    actual_end_date = date(y2, m2, d2)
    if actual_start_date > actual_end_date:
        raise ValueError("Start date can not be greater than end date.")

    # Solution Implementation
    counter_minus = y1 // 400
    y1 = y1 % 400 + 400

    counter_plus = y2 // 400
    y2 = y2 % 400 + 400

    dt = timedelta(days=1)
    start_date = date(y1, m1, d1)
    end_date = date(y2, m2, d2)

    if start_date > end_date:
        counter_plus -= 1
        end_date = date(end_date.year + 400, end_date.month, end_date.day)

    counter = (counter_plus - counter_minus) * 688
    dday = start_date

    while dday <= end_date:
        if dday.weekday() == 6 and dday.day == 1:
            counter += 1
        dday += dt

    return counter


if __name__ == "__main__":
    y1 = 2000
    m1 = 1
    d1 = 1
    y2 = 2020
    m2 = 1
    d2 = 1

    result = number_of_sundays_on_the_first_day_of_month(y1, m1, d1, y2, m2, d2)
    print(result)
