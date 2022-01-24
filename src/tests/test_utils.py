# pylint: disable=no-self-use
import datetime
from typing import Optional

import pytest
from freezegun import freeze_time  # type: ignore[import]

import datetime_helpers
from datetime_helpers import DayOfWeek


class TestGetPreviousBusinessDay:
    # check that we get the previous business day for default today
    @freeze_time(time_to_freeze="2012-01-14")
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
    @freeze_time(time_to_freeze="2012-01-13")
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
        assert datetime_helpers.datetime_to_string(dt=current_dt, datetime_format="%m-%Y-%dT%H:%M:%S.%fZ") == expected_string


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
    # check datetime_from_string
    @pytest.mark.parametrize(
        argnames="text,datetime_format,dt",
        argvalues=[
            ("2016-04-17T00:00:00.000000Z", None, datetime.datetime(2016, 4, 17)),
            ("17-04-2016", "%d-%m-%Y", datetime.datetime(2016, 4, 17)),
        ],
    )
    # check datetime_from_string
    def test_datetime_from_string(self, text: str, datetime_format: Optional[str], dt: datetime.datetime) -> None:
        kwargs = {}
        if datetime_format:
            kwargs['datetime_format'] = datetime_format
        assert datetime_helpers.datetime_from_string(text=text, **kwargs) == dt


class TestGetDayOfWeek:
    # check get_day_of_week
    @pytest.mark.parametrize(
        argnames="dt,day_of_week",
        argvalues=[
            (datetime.date(2021, 2, 1), DayOfWeek.MONDAY),  # monday
            (datetime.date(2021, 2, 2), DayOfWeek.TUESDAY),  # tuesday
            (datetime.date(2021, 2, 3), DayOfWeek.WEDNESDAY),  # wednesday
            (datetime.date(2021, 2, 4), DayOfWeek.THURSDAY),  # thursday
            (datetime.date(2021, 2, 5), DayOfWeek.FRIDAY),  # friday
            (datetime.date(2021, 2, 6), DayOfWeek.SATURDAY),  # saturday
            (datetime.date(2021, 2, 7), DayOfWeek.SUNDAY),  # sunday
        ],
    )
    def test_get_day_of_week(self, dt: datetime.date, day_of_week: str) -> None:
        assert datetime_helpers.get_day_of_week(dt=dt) == day_of_week


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestIsWeekday:
    # check is_weekday
    @pytest.mark.parametrize(
        argnames="dt,is_weekday",
        argvalues=[
            (datetime.date(2021, 2, 1), True),  # monday
            (datetime.date(2021, 2, 2), True),  # tuesday
            (datetime.date(2021, 2, 3), True),  # wednesday
            (datetime.date(2021, 2, 4), True),  # thursday
            (datetime.date(2021, 2, 5), True),  # friday
            (datetime.date(2021, 2, 6), False),  # saturday
            (datetime.date(2021, 2, 7), False),  # sunday
        ],
    )
    def test_is_weekday(self, dt: datetime.date, is_weekday: bool) -> None:
        assert datetime_helpers.is_weekday(dt=dt) is is_weekday


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestIsWeekend:
    # check is_weekend
    @pytest.mark.parametrize(
        argnames="dt,is_weekend",
        argvalues=[
            (datetime.date(2021, 2, 1), False),  # monday
            (datetime.date(2021, 2, 2), False),  # tuesday
            (datetime.date(2021, 2, 3), False),  # wednesday
            (datetime.date(2021, 2, 4), False),  # thursday
            (datetime.date(2021, 2, 5), False),  # friday
            (datetime.date(2021, 2, 6), True),  # saturday
            (datetime.date(2021, 2, 7), True),  # sunday
        ],
    )
    def test_is_weekend(self, dt: datetime.date, is_weekend: bool) -> None:
        assert datetime_helpers.is_weekend(dt=dt) is is_weekend  # sunday


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestGetFirstBusinessDayOfMonth:
    # check get_first_business_day_of_month
    @pytest.mark.parametrize(
        argnames="dt,first_business_day_of_month",
        argvalues=[
            (datetime.date(2021, 1, 20), datetime.date(2021, 1, 1)),
            (datetime.date(2021, 2, 20), datetime.date(2021, 2, 1)),
            (datetime.date(2021, 3, 20), datetime.date(2021, 3, 1)),
            (datetime.date(2021, 4, 20), datetime.date(2021, 4, 1)),
            (datetime.date(2021, 5, 20), datetime.date(2021, 5, 3)),
            (datetime.date(2021, 6, 20), datetime.date(2021, 6, 1)),
            (datetime.date(2021, 7, 20), datetime.date(2021, 7, 1)),
            (datetime.date(2021, 8, 20), datetime.date(2021, 8, 2)),
            (datetime.date(2021, 9, 20), datetime.date(2021, 9, 1)),
            (datetime.date(2021, 10, 20), datetime.date(2021, 10, 1)),
            (datetime.date(2021, 11, 20), datetime.date(2021, 11, 1)),
            (datetime.date(2021, 12, 20), datetime.date(2021, 12, 1)),
        ],
    )
    def test_first_business_day_of_month(self, dt: datetime.date, first_business_day_of_month: datetime.date) -> None:
        assert datetime_helpers.get_first_business_day_of_month(dt=dt) == first_business_day_of_month


# see https://www.timeanddate.com/calendar/?year=2021&country=9
class TestGetNthBusinessDayOfMonth:
    # check nth_business_day_of_month
    @pytest.mark.parametrize(
        argnames="current_dt,n,nth_business_day_of_month",
        argvalues=[
            (datetime.date(2021, 2, 5), 1, datetime.date(2021, 2, 1)),
            (datetime.date(2021, 2, 5), 2, datetime.date(2021, 2, 2)),
            (datetime.date(2021, 2, 5), 3, datetime.date(2021, 2, 3)),
            (datetime.date(2021, 2, 5), 4, datetime.date(2021, 2, 4)),
            (datetime.date(2021, 2, 5), 5, datetime.date(2021, 2, 5)),
            (datetime.date(2021, 2, 5), 6, datetime.date(2021, 2, 8)),
            (datetime.date(2021, 2, 5), 7, datetime.date(2021, 2, 9)),
            (datetime.date(2021, 2, 5), 8, datetime.date(2021, 2, 10)),
            (datetime.date(2021, 2, 5), 9, datetime.date(2021, 2, 11)),
            (datetime.date(2021, 2, 5), 10, datetime.date(2021, 2, 12)),
            (datetime.date(2021, 2, 5), 11, datetime.date(2021, 2, 15)),
            (datetime.date(2021, 2, 5), 12, datetime.date(2021, 2, 16)),
            (datetime.date(2021, 2, 5), 13, datetime.date(2021, 2, 17)),
            (datetime.date(2021, 2, 5), 14, datetime.date(2021, 2, 18)),
            (datetime.date(2021, 2, 5), 15, datetime.date(2021, 2, 19)),
        ],
    )
    def test_nth_business_day_of_month(self, current_dt: datetime.date, n: int, nth_business_day_of_month: datetime.date) -> None:  # pylint: disable=invalid-name
        assert datetime_helpers.get_nth_business_day_of_month(dt=current_dt, n=n) == nth_business_day_of_month


class TestDatetimeFromWindowsFiletime:
    # check datetime_from_windows_filetime
    @pytest.mark.parametrize(
        argnames="windows_filetime,datetime_from_windows_filetime",
        argvalues=[
            (116444736000000000, datetime.datetime(1970, 1, 1, 0, 0)),
            (128930364000000000, datetime.datetime(2009, 7, 25, 23, 0)),
            (128930364000001000, datetime.datetime(2009, 7, 25, 23, 0, 0, 100)),
        ],
    )
    def test_datetime_from_windows_filetime(self, windows_filetime: int, datetime_from_windows_filetime: datetime.datetime) -> None:
        assert datetime_helpers.datetime_from_windows_filetime(windows_filetime=windows_filetime) == datetime_from_windows_filetime
