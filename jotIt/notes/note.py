from jotIt.notes.date import DateEntry
from jotIt.notes.tag import Tag


class NoteEntry:
    def __init__(self, date, message, tags):
        # TODO: what is the format of date? (Y, M, D).
        # TODO: what is the format of message? (title, body)
        self._date = DateEntry(*date)
        self._note = Note(*message)
        self._tags = Tag(*tags)

    def get_entry_time(self):
        return self.date.getDate()

    def filter_date_in_range(self, low, high):
        # TODO
        pass

    def filter_contains_text(self, text):
        # TODO
        pass

    def filter_contains_tag(self, tag):
        # TODO
        # self.getTag().filter_contains(tag)


class Note:
    def __init__(self, body, title):
        self._body = body
        self._title = title

    def get_body(self):
        return self._body

    def get_title(self):
        return self._title
