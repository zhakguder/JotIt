import datetime
import warnings
from unittest import TestCase, mock
from jotIt import DateEntry
from jotIt.test.constants import *


class TestDate(TestCase):
    def test_invalid_format(self):
        year_month_day = DateEntry(YEAR, YEAR, "12")

    def test_invalid_value(self):
        year_month_day = DateEntry(YEAR, YEAR, YEAR)

    def test_year_month_day(self):

        year_month_day = DateEntry(YEAR, MONTH, DAY)
        self.assertEqual(year_month_day.getYear(), YEAR)
        self.assertEqual(year_month_day.getMonth(), MONTH)
        self.assertEqual(year_month_day.getDay(), DAY)

    def test_year_month(self):
        year_month = DateEntry(YEAR, MONTH)
        self.assertEqual(year_month.getYear(), YEAR)
        self.assertEqual(year_month.getMonth(), MONTH)

    def test_year(self):
        year = DateEntry(YEAR)
        self.assertEqual(year.getYear(), YEAR)

    def test_year(self):
        nothing_given = DateEntry()
        # TODO how to catch warning message
        with warnings.catch_warnings(record=True) as wl:
            year = nothing_given.getYear()
        self.assertEqual(year, 2020)

    def test_get_date(self):
        year_month_day = DateEntry(YEAR, MONTH, DAY)
        self.assertEqual(
            year_month_day.getDate(),
            datetime.date(YEAR, MONTH, DAY).strftime(DATE_FORMAT),
        )


if __name__ == "__main__":
    unittest.main()
