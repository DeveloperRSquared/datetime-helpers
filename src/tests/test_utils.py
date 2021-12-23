# pylint: disable=no-self-use
import datetime

from freezegun import freeze_time  # type: ignore[import]

import datetime_helpers


class TestGetPreviousBusinessDay:
    # check that we get the previous business day for default today
    @freeze_time("2012-01-14")
    def test_defaults(self) -> None:
        previous_dt = datetime_helpers.get_previous_business_day()
        assert previous_dt.weekday() == 4

    # check previous business day on sunday
    def test_sunday(self) -> None:
        current_dt = datetime.date(2021, 3, 28)
        previous_dt = datetime_helpers.get_previous_business_day(dt=current_dt)
        assert previous_dt.weekday() == 4

    # check previous business day on saturday
    def test_saturday(self) -> None:
        current_dt = datetime.date(2021, 3, 27)
        previous_dt = datetime_helpers.get_previous_business_day(dt=current_dt)
        assert previous_dt.weekday() == 4

    # check previous business day on monday
    def test_monday(self) -> None:
        current_dt = datetime.date(2021, 3, 29)
        previous_dt = datetime_helpers.get_previous_business_day(dt=current_dt)
        assert previous_dt.weekday() == 4

    # check previous business day mid week date
    def test_mid_week_date(self) -> None:
        current_dt = datetime.date(2021, 3, 31)
        previous_dt = datetime_helpers.get_previous_business_day(dt=current_dt)
        assert previous_dt.weekday() == 1


class TestGetNextBusinessDay:
    # check that we get the next business day for default today
    @freeze_time("2012-01-13")
    def test_defaults(self) -> None:
        next_dt = datetime_helpers.get_next_business_day()
        assert next_dt.weekday() == 0

    # check next business day on sunday
    def test_sunday(self) -> None:
        current_dt = datetime.date(2021, 3, 28)
        next_dt = datetime_helpers.get_next_business_day(dt=current_dt)
        assert next_dt.weekday() == 0

    # check next business day on saturday
    def test_saturday(self) -> None:
        current_dt = datetime.date(2021, 3, 27)
        next_dt = datetime_helpers.get_next_business_day(dt=current_dt)
        assert next_dt.weekday() == 0

    # check next business day on monday
    def test_monday(self) -> None:
        current_dt = datetime.date(2021, 3, 29)
        next_dt = datetime_helpers.get_next_business_day(dt=current_dt)
        assert next_dt.weekday() == 1

    # check next business day mid week date
    def test_mid_week_date(self) -> None:
        current_dt = datetime.date(2021, 3, 31)
        next_dt = datetime_helpers.get_next_business_day(dt=current_dt)
        assert next_dt.weekday() == 3


class TestDatetimeToString:
    # check dt to string default format
    def test_datetime_to_string(self) -> None:
        current_dt = datetime.datetime(2016, 4, 17, 3, 12, 34)
        expected_string = "2016-04-17T03:12:34.000000Z"
        assert datetime_helpers.datetime_to_string(dt=current_dt) == expected_string

    # check dt to string custom format
    def test_datetime_to_string_custom_format(self) -> None:
        current_dt = datetime.datetime(2016, 4, 17, 3, 12, 34)
        expected_string = "04-2016-17T03:12:34.000000Z"
        assert datetime_helpers.datetime_to_string(dt=current_dt, date_format="%m-%Y-%dT%H:%M:%S.%fZ") == expected_string


class TestDateToString:
    # check date to string default format
    def test_date_to_string(self) -> None:
        current_dt = datetime.date(2016, 4, 17)
        expected_string = "2016-04-17"
        assert datetime_helpers.date_to_string(dt=current_dt) == expected_string

    # check dt to string custom format
    def test_date_to_string_custom_format(self) -> None:
        current_dt = datetime.date(2016, 4, 17)
        expected_string = "17-04-2016"
        assert datetime_helpers.date_to_string(dt=current_dt, date_format="%d-%m-%Y") == expected_string


class TestDateFromString:
    # check date from string default format
    def test_date_from_string(self) -> None:
        expected_dt = datetime.date(2016, 4, 17)
        text = "2016-04-17"
        assert datetime_helpers.date_from_string(text=text) == expected_dt

    # check dt from string custom format
    def test_date_from_string_custom_format(self) -> None:
        expected_dt = datetime.date(2016, 4, 17)
        text = "17-04-2016"
        assert datetime_helpers.date_from_string(text=text, date_format="%d-%m-%Y") == expected_dt


class TestDatetimeFromString:
    # check datetime from string default format
    def test_datetime_from_string(self) -> None:
        expected_dt = datetime.datetime(2016, 4, 17)
        text = "2016-04-17T00:00:00.000000Z"
        assert datetime_helpers.datetime_from_string(text=text) == expected_dt

    # check dt from string custom format
    def test_datetime_from_string_custom_format(self) -> None:
        expected_dt = datetime.datetime(2016, 4, 17)
        text = "17-04-2016"
        assert datetime_helpers.datetime_from_string(text=text, datetime_format="%d-%m-%Y") == expected_dt


class TestGetDayOfWeek:
    # check first week of Feb 2021
    def test_get_day_of_week(self) -> None:
        assert datetime_helpers.get_day_of_week(dt=datetime.date(2021, 2, 1)) == "Monday"
        assert datetime_helpers.get_day_of_week(dt=datetime.date(2021, 2, 2)) == "Tuesday"
        assert datetime_helpers.get_day_of_week(dt=datetime.date(2021, 2, 3)) == "Wednesday"
        assert datetime_helpers.get_day_of_week(dt=datetime.date(2021, 2, 4)) == "Thursday"
        assert datetime_helpers.get_day_of_week(dt=datetime.date(2021, 2, 5)) == "Friday"
        assert datetime_helpers.get_day_of_week(dt=datetime.date(2021, 2, 6)) == "Saturday"
        assert datetime_helpers.get_day_of_week(dt=datetime.date(2021, 2, 7)) == "Sunday"


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestIsWeekday:
    # check first week of Feb 2021
    def test_is_weekday(self) -> None:
        assert datetime_helpers.is_weekday(dt=datetime.date(2021, 2, 1)) is True  # monday
        assert datetime_helpers.is_weekday(dt=datetime.date(2021, 2, 2)) is True  # tuesday
        assert datetime_helpers.is_weekday(dt=datetime.date(2021, 2, 3)) is True  # wednesday
        assert datetime_helpers.is_weekday(dt=datetime.date(2021, 2, 4)) is True  # thursday
        assert datetime_helpers.is_weekday(dt=datetime.date(2021, 2, 5)) is True  # friday
        assert datetime_helpers.is_weekday(dt=datetime.date(2021, 2, 6)) is False  # saturday
        assert datetime_helpers.is_weekday(dt=datetime.date(2021, 2, 7)) is False  # sunday


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestIsWeekend:
    # check first week of Feb 2021
    def test_is_weekend(self) -> None:
        assert datetime_helpers.is_weekend(dt=datetime.date(2021, 2, 1)) is False  # monday
        assert datetime_helpers.is_weekend(dt=datetime.date(2021, 2, 2)) is False  # tuesday
        assert datetime_helpers.is_weekend(dt=datetime.date(2021, 2, 3)) is False  # wednesday
        assert datetime_helpers.is_weekend(dt=datetime.date(2021, 2, 4)) is False  # thursday
        assert datetime_helpers.is_weekend(dt=datetime.date(2021, 2, 5)) is False  # friday
        assert datetime_helpers.is_weekend(dt=datetime.date(2021, 2, 6)) is True  # saturday
        assert datetime_helpers.is_weekend(dt=datetime.date(2021, 2, 7)) is True  # sunday


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestGetFirstBusinessDayOfMonth:
    # check for 2021
    def test_nth_business_day_of_month(self) -> None:
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 1, 20)) == datetime.date(2021, 1, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 2, 20)) == datetime.date(2021, 2, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 3, 20)) == datetime.date(2021, 3, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 4, 20)) == datetime.date(2021, 4, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 5, 20)) == datetime.date(2021, 5, 3)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 6, 20)) == datetime.date(2021, 6, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 7, 20)) == datetime.date(2021, 7, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 8, 20)) == datetime.date(2021, 8, 2)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 9, 20)) == datetime.date(2021, 9, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 10, 20)) == datetime.date(2021, 10, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 11, 20)) == datetime.date(2021, 11, 1)
        assert datetime_helpers.get_first_business_day_of_month(dt=datetime.date(2021, 12, 20)) == datetime.date(2021, 12, 1)


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestGetNthBusinessDayOfMonth:
    # check for Feb 2021
    def test_nth_business_day_of_month(self) -> None:
        current_dt = datetime.date(2021, 2, 5)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=1) == datetime.date(2021, 2, 1)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=2) == datetime.date(2021, 2, 2)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=3) == datetime.date(2021, 2, 3)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=4) == datetime.date(2021, 2, 4)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=5) == datetime.date(2021, 2, 5)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=6) == datetime.date(2021, 2, 8)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=7) == datetime.date(2021, 2, 9)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=8) == datetime.date(2021, 2, 10)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=9) == datetime.date(2021, 2, 11)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=10) == datetime.date(2021, 2, 12)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=11) == datetime.date(2021, 2, 15)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=12) == datetime.date(2021, 2, 16)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=13) == datetime.date(2021, 2, 17)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=14) == datetime.date(2021, 2, 18)
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=15) == datetime.date(2021, 2, 19)
