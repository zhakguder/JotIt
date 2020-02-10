import abc
from abc import ABC
import datetime
import warnings
from jotIt.notes.constants import *


class DateEntry:
    def __init__(self, year=0, month=0, day=0):
        self._year = year if year else TODAY.year
        self._month = month if month else TODAY.month
        self._day = day if day else TODAY.day
        if Date.is_valid(self._year, self._month, self._day):
            self.date = Date.make_date(self._year, self._month, self._day)

    def get_year(self):
        return self._year

    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

    def get_date(self):
        return datetime.date(self._year, self._month, self._day).strftime("%b %d %Y")

    def is_in_range(self, low_date, high_date):
        # low date and high date should be lists in format [Y, M, D]

        # TODO: need to ask to get date again if invalid
        low_date = Date.make_date(*low_date) if Date.is_valid(*low_date) else None
        high_date = Date.make_date(*high_date) if Date.is_valid(*high_date) else None
        # TODO: raise exception here??
        return self.date > low_date and self.date <= high_date

    def __le__(self, other):
        return Date.is_before(self.date, other.date)

    def __gt__(self, other):
        return Date.is_after(self.date, other.date)

    def __str__(self):
        return self._date


class Date(ABC):
    @staticmethod
    def make_date(year, month, day):
        return datetime.date(year, month, day)

    @staticmethod
    def is_valid(year, month, day):
        try:
            datetime.datetime(year=year, month=month, day=day)
        # TODO how to better handle these warnings?
        except ValueError as e:
            warnings.warn("Please enter a valid date.")
            return False
        except TypeError as e:
            warnings.warn("Please enter only integers.")
            return False
        return True

    @staticmethod
    def is_before(date, otherdate):
        return date <= otherdate

    @staticmethod
    def is_after(date, otherdate):
        return date > otherdate
