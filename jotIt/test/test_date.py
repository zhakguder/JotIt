import datetime
import warnings
from unittest import TestCase, mock
from jotIt import DateFactory
from jotIt.test.constants import *


class TestDate(TestCase):
    def test_year_month_day(self):

        year_month_day = DateFactory.factory(YEAR, MONTH, DAY)
        self.assertEqual(year_month_day.getYear(), YEAR)
        self.assertEqual(year_month_day.getMonth(), MONTH)
        self.assertEqual(year_month_day.getDay(), DAY)

    def test_year_month(self):
        year_month = DateFactory.factory(YEAR, MONTH)
        self.assertEqual(year_month.getYear(), YEAR)
        self.assertEqual(year_month.getMonth(), MONTH)

    def test_year(self):
        year = DateFactory.factory(YEAR)
        self.assertEqual(year.getYear(), YEAR)

    def test_year(self):
        nothing_given = DateFactory.factory()
        # TODO how to catch warning message
        with warnings.catch_warnings(record=True) as wl:
            year = nothing_given.getYear()
        self.assertEqual(year, 2020)

    def get_date(self):
        year_month_day = DateFactory.factory(YEAR, MONTH, DAY)
        self.assertEqual(
            year_month_day.getDate(),
            datetime.date(YEAR, MONTH, DAY).strftime(DATE_FORMAT),
        )


if __name__ == "__main__":
    unittest.main()
