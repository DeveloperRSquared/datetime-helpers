import calendar
import datetime
from typing import Optional

from http_exceptions.client_exceptions import BadRequestException

JSON_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
EPOCH = datetime.datetime.fromtimestamp(0)


def get_day_of_week(dt: datetime.date) -> str:  # pylint: disable=invalid-name
    day_of_week_int = dt.weekday()
    return calendar.day_name[day_of_week_int]


def is_weekend(dt: datetime.date) -> bool:  # pylint: disable=invalid-name
    return get_day_of_week(dt=dt) in ["Saturday", "Sunday"]


def is_weekday(dt: datetime.date) -> bool:  # pylint: disable=invalid-name
    return not is_weekend(dt=dt)


def get_previous_business_day(dt: Optional[datetime.date] = None) -> datetime.date:  # pylint: disable=invalid-name
    dt = dt or datetime.date.today()
    if get_day_of_week(dt=dt) == "Sunday":
        previous_business_day_of_month = dt - datetime.timedelta(days=2)
    elif get_day_of_week(dt=dt) == "Monday":
        previous_business_day_of_month = dt - datetime.timedelta(days=3)
    else:
        previous_business_day_of_month = dt - datetime.timedelta(days=1)
    return previous_business_day_of_month


def get_next_business_day(dt: Optional[datetime.date] = None) -> datetime.date:  # pylint: disable=invalid-name
    dt = dt or datetime.date.today()
    if get_day_of_week(dt=dt) == "Friday":
        next_business_day_of_month = dt + datetime.timedelta(days=3)
    elif get_day_of_week(dt=dt) == "Saturday":
        next_business_day_of_month = dt + datetime.timedelta(days=2)
    else:
        next_business_day_of_month = dt + datetime.timedelta(days=1)
    return next_business_day_of_month


def get_first_business_day_of_month(dt: Optional[datetime.date] = None) -> datetime.date:  # pylint: disable=invalid-name
    dt = dt or datetime.date.today()
    first_day_of_month = datetime.date(dt.year, dt.month, 1)
    if is_weekday(dt=first_day_of_month):
        first_business_day_of_month = first_day_of_month
    else:
        first_business_day_of_month = get_next_business_day(dt=first_day_of_month)
    return first_business_day_of_month


def get_nth_business_day_of_month(n: int, dt: Optional[datetime.date] = None) -> datetime.date:  # pylint: disable=invalid-name
    dt = dt or datetime.date.today()
    nth_business_day_of_month = get_first_business_day_of_month(dt=dt)
    for _ in range(n - 1):
        nth_business_day_of_month = get_next_business_day(dt=nth_business_day_of_month)
    if nth_business_day_of_month.month != dt.month:
        raise BadRequestException(message="n > # of business days in month")
    return nth_business_day_of_month


def datetime_to_string(dt: datetime.datetime, datetime_format: str = JSON_DATE_FORMAT) -> str:  # pylint: disable=invalid-name
    return dt.strftime(datetime_format)


def date_to_string(dt: datetime.date, date_format: str = "%Y-%m-%d") -> str:  # pylint: disable=invalid-name  # pylint: disable=invalid-name
    return dt.strftime(date_format)


def datetime_from_string(text: str, datetime_format: str = JSON_DATE_FORMAT) -> datetime.datetime:
    return datetime.datetime.strptime(text, datetime_format)


def date_from_string(text: str, date_format: str = "%Y-%m-%d") -> datetime.date:
    return datetime_from_string(text=text, datetime_format=date_format).date()
