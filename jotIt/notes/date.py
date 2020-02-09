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
        Date.is_valid(self.getYear(), self.getMonth(), self.getDay())

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


class Date(ABC):
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
        return True
