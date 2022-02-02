# Datetime Helpers

A handy collection of datetime utils.

[![Publish](https://github.com/DeveloperRSquared/datetime-helpers/actions/workflows/publish.yml/badge.svg)](https://github.com/DeveloperRSquared/datetime-helpers/actions/workflows/publish.yml)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-brightgreen.svg)](#datetime-helpers)
[![PyPI - License](https://img.shields.io/pypi/l/datetime-helpers.svg)](LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/datetime-helpers.svg)](https://pypi.org/project/datetime-helpers)

[![CodeQL](https://github.com/DeveloperRSquared/datetime-helpers/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/DeveloperRSquared/datetime-helpers/actions/workflows/codeql-analysis.yml)
[![codecov](https://codecov.io/gh/DeveloperRSquared/datetime-helpers/branch/main/graph/badge.svg?token=UI5ZDDDXXB)](https://codecov.io/gh/DeveloperRSquared/datetime-helpers)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DeveloperRSquared/datetime-helpers/main.svg)](https://results.pre-commit.ci/latest/github/DeveloperRSquared/datetime-helpers/main)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

## Install

Install and update using [pip](https://pypi.org/project/datetime-helpers/).

```sh
$ pip install -U datetime-helpers
```

## What's available?

```py
import datetime_helpers

# Given a datetime:
>>> dt = datetime.date(2017, 4, 17)

# Check the day of week
>>> datetime_helpers.get_day_of_week(dt=dt)
'Monday'

# Check if it is a weekend
>>> datetime_helpers.is_weekend(dt=dt)
False

# Check if it is a weekday
>>> datetime_helpers.is_weekday(dt=dt)
True

# Get the previous business day
>>> datetime_helpers.get_previous_business_day(dt=dt)
datetime.date(2017, 4, 14)

# Get the next business day
>>> datetime_helpers.get_next_business_day(dt=dt)
datetime.date(2017, 4, 18)

# Get the first business day of the month
>>> datetime_helpers.get_first_business_day_of_month(dt=dt)
datetime.date(2017, 4, 3)

# Get the nth business day of the month
>>> n = 3  # e.g. third business day
>>> datetime_helpers.get_nth_business_day_of_month(dt=dt, n=n)
datetime.date(2017, 4, 5)

# Convert to a datetime string with custom format (defaults to JSON date format)
>>> datetime_helpers.datetime_to_string(dt=dt)
'2017-04-17T00:00:00.000000Z'

# Convert to a date string with custom format (defaults to YYYY-MM-DD)
>>> datetime_helpers.date_to_string(dt=dt)
'2017-04-17'

# Convert a string with custom format to datetime (defaults to JSON date format)
>>> text = '2016-04-17T00:00:00.000000Z'
>>> datetime_helpers.datetime_from_string(text=text)
datetime.datetime(2016, 4, 17, 0, 0)

# Convert a string with custom format to datetime (defaults to JSON date format)
>>> text = '2016-04-17T00:00:00.000000Z'
>>> datetime_helpers.datetime_from_string(text=text)
datetime.datetime(2016, 4, 17, 0, 0)

# Convert a windows filetime to datetime
>>> windows_filetime = 116444736000000000
>>> datetime_helpers.datetime_from_windows_filetime(windows_filetime=windows_filetime)
datetime.datetime(1970, 1, 1, 0, 0)

# Convert to seconds
>>> datetime_helpers.datetime_to_seconds(dt=dt)
1492387200.0

# Convert seconds to datetime
>>> seconds = 1492387200
>>> datetime_helpers.datetime_from_seconds(seconds=seconds)
datetime.datetime(2017, 4, 17, 0, 0)

# Convert to millis
>>> datetime_helpers.datetime_to_millis(dt=dt)
1492387200000

# Convert millis to datetime
>>> millis = 1492387200000
>>> datetime_helpers.datetime_from_millis(millis=millis)
datetime.datetime(2017, 4, 17, 0, 0)

# Convert date to datetime
>>> datetime_helpers.datetime_from_date(dt=dt)
datetime.datetime(2017, 4, 17, 0, 0)
```

## Contributing

Contributions are welcome via pull requests.

### First time setup

```sh
$ git clone git@github.com:DeveloperRSquared/datetime-helpers.git
$ cd datetime-helpers
$ poetry install
$ poetry shell
```

Tools including black, mypy etc. will run automatically if you install [pre-commit](https://pre-commit.com) using the instructions below

```sh
$ pre-commit install
$ pre-commit run --all-files
```

### Running tests

```sh
$ poetry run pytest
```

## Links

- Source Code: <https://github.com/DeveloperRSquared/datetime-helpers/>
- PyPI Releases: <https://pypi.org/project/datetime-helpers/>
- Issue Tracker: <https://github.com/DeveloperRSquared/datetime-helpers/issues/>
