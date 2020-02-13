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
        date = DateEntry(YEAR, YEAR, "12")

    def test_invalid_value(self):
        date = DateEntry(YEAR, YEAR, YEAR)

    def test_year_month_day(self):
        date = DateEntry(YEAR, MONTH, DAY)
        self.assertEqual(date.get_date(), datetime.date(YEAR, MONTH, DAY))
        self.assertEqual(date.get_year(), YEAR)
        self.assertEqual(date.get_month(), MONTH)
        self.assertEqual(date.get_day(), DAY)

    def test_year_month(self):
        date = DateEntry(YEAR, MONTH)
        self.assertEqual(date.get_year(), YEAR)
        self.assertEqual(date.get_month(), MONTH)

    def test_year(self):
        date = DateEntry(YEAR)
        self.assertEqual(year.get_year(), YEAR)

    def test_year(self):
        date = DateEntry()
        # TODO how to catch warning message
        with warnings.catch_warnings(record=True) as wl:
            year = date.get_year()
        self.assertEqual(year, 2020)

    def test_get_date(self):
        year_month_day = DateEntry(YEAR, MONTH, DAY)
        self.assertEqual(year_month_day.get_date(), datetime.date(YEAR, MONTH, DAY))

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
