import calendar
import datetime
from typing import Optional
from typing import cast

from http_exceptions.client_exceptions import BadRequestException

JSON_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
EPOCH = datetime.datetime.utcfromtimestamp(0)  # 00:00:00 UTC on 1 January 1970


class DayOfWeek:
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


def create_date(year: int, month: int, day: int) -> datetime.date:
    try:
        return datetime.date(year=year, month=month, day=day)
    except (ValueError, TypeError) as exception:
        raise BadRequestException(message=str(exception)) from None


def create_datetime(year: int, month: int, day: int, hour: Optional[int] = None, minute: Optional[int] = None, second: Optional[int] = None, microsecond: Optional[int] = None) -> datetime.datetime:
    try:
        return datetime.datetime(year=year, month=month, day=day, hour=hour or 0, minute=minute or 0, second=second or 0, microsecond=microsecond or 0)
    except (ValueError, TypeError) as exception:
        raise BadRequestException(message=str(exception)) from None


def get_day_of_week(dt: datetime.date) -> str:
    day_of_week_int = dt.weekday()
    return calendar.day_name[day_of_week_int]


def is_weekend(dt: datetime.date) -> bool:
    return get_day_of_week(dt=dt) in [DayOfWeek.SATURDAY, DayOfWeek.SUNDAY]


def is_weekday(dt: datetime.date) -> bool:
    return not is_weekend(dt=dt)


def get_previous_business_day(dt: Optional[datetime.date] = None) -> datetime.date:
    dt = dt or datetime.date.today()
    if get_day_of_week(dt=dt) == DayOfWeek.SUNDAY:
        previous_business_day_of_month = dt - datetime.timedelta(days=2)
    elif get_day_of_week(dt=dt) == DayOfWeek.MONDAY:
        previous_business_day_of_month = dt - datetime.timedelta(days=3)
    else:
        previous_business_day_of_month = dt - datetime.timedelta(days=1)
    return previous_business_day_of_month


def get_next_business_day(dt: Optional[datetime.date] = None) -> datetime.date:
    dt = dt or datetime.date.today()
    if get_day_of_week(dt=dt) == DayOfWeek.FRIDAY:
        next_business_day_of_month = dt + datetime.timedelta(days=3)
    elif get_day_of_week(dt=dt) == DayOfWeek.SATURDAY:
        next_business_day_of_month = dt + datetime.timedelta(days=2)
    else:
        next_business_day_of_month = dt + datetime.timedelta(days=1)
    return next_business_day_of_month


def get_first_business_day_of_month(dt: Optional[datetime.date] = None) -> datetime.date:
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


def datetime_to_string(dt: datetime.datetime, datetime_format: str = JSON_DATE_FORMAT) -> str:
    return dt.strftime(datetime_format)


def date_to_string(dt: datetime.date, date_format: str = "%Y-%m-%d") -> str:
    return dt.strftime(date_format)


def datetime_from_string(text: str, datetime_format: str = JSON_DATE_FORMAT) -> datetime.datetime:
    return datetime.datetime.strptime(text, datetime_format)


def date_from_string(text: str, date_format: str = "%Y-%m-%d") -> datetime.date:
    return datetime_from_string(text=text, datetime_format=date_format).date()


def datetime_from_windows_filetime(windows_filetime: int) -> datetime.datetime:
    windows_epoch = datetime.datetime(1601, 1, 1)
    return windows_epoch + datetime.timedelta(microseconds=windows_filetime / 10)


def datetime_to_seconds(dt: datetime.date) -> float:
    if type(dt) == datetime.date:  # pylint: disable=unidiomatic-typecheck
        dt = datetime_from_date(dt=dt)
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = cast(datetime.timedelta, dt - epoch)
    return delta.total_seconds()


def datetime_from_seconds(seconds: float) -> datetime.datetime:
    return datetime.datetime.utcfromtimestamp(seconds)


def datetime_to_millis(dt: datetime.date) -> int:
    return int(datetime_to_seconds(dt=dt) * 1000.0)


def datetime_from_millis(millis: float) -> datetime.datetime:
    return datetime_from_seconds(seconds=millis / 1000.0)


def datetime_from_date(dt: datetime.date) -> datetime.datetime:
    if isinstance(dt, datetime.datetime):
        return dt
    return datetime.datetime.combine(dt, datetime.time.min)
