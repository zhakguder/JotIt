import datetime
import warnings
from unittest import TestCase, mock
from jotIt import DateEntry, Date
from jotIt.test.constants import *

YEAR = CURR_DATE["year"]
MONTH = CURR_DATE["month"]
DAY = CURR_DATE["day"]


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

    def test_make_date(self):
        date = Date.make_date(YEAR, MONTH, DAY)

    def test_is_before(self):
        curr_date = Date.make_date(*CURR_DATE.values())
        low_date = Date.make_date(*LOW_DATE.values())
        self.assertTrue(Date.is_before(low_date, curr_date))

    def test_is_after(self):
        curr_date = Date.make_date(*CURR_DATE.values())
        low_date = Date.make_date(*LOW_DATE.values())
        self.assertTrue(Date.is_after(curr_date, low_date))


if __name__ == "__main__":
    unittest.main()
