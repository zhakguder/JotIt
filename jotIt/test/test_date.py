from unittest import TestCase, mock
from jotIt import DateFactory
import warnings

YEAR = 2010
MONTH = 3
DAY = 12


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


if __name__ == "__main__":
    unittest.main()
