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
        if Date.is_valid(self.getYear(), self.getMonth(), self.getDay()):
            self.date = Date.make_date(self.getYear(), self.getMonth(), self.getDay())

    def getYear(self):
        return self._year

    def getMonth(self):
        return self._month

    def getDay(self):
        return self._day

    def getDate(self):
        return datetime.date(self.getYear(), self.getMonth(), self.getDay()).strftime(
            "%b %d %Y"
        )

    def is_in_range(self, low_date, high_date):
        # low date and high date should be lists in format [Y, M, D]

        # TODO: need to ask to get date again if invalid
        low_date = Date.make_date(*low_date) if Date.is_valid(*low_date) else None
        high_date = Date.make_date(*high_date) if Date.is_valid(*high_date) else None
        return Date.is_after(self.date, low_date) and Date.is_before(
            self.date, high_date
        )


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
        return date >= otherdate
