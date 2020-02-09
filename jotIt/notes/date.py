import abc
import datetime
import warnings


class DateFactory:
    @staticmethod
    def factory(year=None, month=None, day=None):
        if not year:
            year = datetime.datetime.now().year
            # TODO: do I want to use something else instead of warnings
            warnings.warn(f"You didn't specify the year. Using {year}")
            return DateWithYear(year)
        if month and day:
            return DateWithYearMonthDay(year, month, day)
        elif month:
            return DateWithYearMonth(year, month)
        else:
            return DateWithYear(year)


class Date(metaclass=abc.ABCMeta):
    def getYear(self):
        return self._year

    @abc.abstractmethod
    def getMonth(self):
        return

    @abc.abstractmethod
    def getDay(self):
        return


class DateWithYearMonthDay(Date):
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    def getMonth(self):
        return self._month

    def getDay(self):
        return self._day


class DateWithYearMonth(Date):
    def __init__(self, year, month):
        self._year = year
        self._month = month

    def getMonth(self):
        return self._month

    def getDay(self):
        return 1


class DateWithYear(Date):
    def __init__(self, year):
        self._year = year

    def getMonth(self):
        return 1

    def getDay(self):
        return 1
