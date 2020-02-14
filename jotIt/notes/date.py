import datetime
import warnings
from jotIt.notes.constants import *


class DateEntry:
    def __init__(self, year=0, month=0, day=0):
        year = year if year else TODAY.year
        month = month if month else TODAY.month
        day = day if day else TODAY.day
        if Date.is_valid(year, month, day):
            self.date = Date.make_date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_date(self):
        # return datetime.date(self._year, self._month, self._day).strftime("%b %d %Y")
        return self.date

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
        return Date.date_object_to_date_string(self.date)


class Date:
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

    @staticmethod
    def date_object_to_date_string(date, date_format=DATE_FORMAT):
        return date.strftime(date_format)

    @staticmethod
    def date_str_to_date_object(date_str, date_format=DATE_FORMAT):
        return datetime.datetime.strptime(date_str, date_format)
