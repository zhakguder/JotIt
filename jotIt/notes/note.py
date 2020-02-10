from jotIt.notes.date import DateEntry
from jotIt.notes.tag import TagGroup
import operator


class NoteEntries:
    def __init__(self):
        self._entries = []

    def add_note(self, note):
        self.get_entries().append(note)

    def get_entries(self):
        return self._entries

    def summary(self):

        pass

    def sort_entries(self):
        # TODO: how to sort properly
        # maybe with Sorter class?
        return sorted(self.get_entries(), key=operator.attrgetter("_note", "_date"))

    def __iter__(self):
        return self._entries.__iter__()


class Sorter:
    def sort_entries(self,):
        return sorted()


class NoteEntry:
    # TODO maybe make this an implementation of a possible Entry interface
    # Other implementations could include Reminders with due dates and times

    def __init__(self, date, message, tags):
        # TODO: what is the format of date? (Y, M, D).
        # TODO: what is the format of message? (title, body)
        self._date = DateEntry(*date)
        self._note = Note(*message)  # TODO refactor to note_text in tests
        self._tags = TagGroup(tags)

    def get_entry_time(self):
        return self._date.getDate()

    def get_tags(self):
        return self._tags

    def _get_note(self):
        return self._note

    def get_title(self):
        return self._note.get_title()

    def get_note_body(self):
        return self._note.get_body()

    def date_in_range(self, low_date, high_date):
        # low date and high date should be lists in format [Y, M, D]
        # TODO
        return self._date.is_in_range(low_date, high_date)

    def contains_text(self, text):
        return self._get_note().contains(text) or self.get_tags().contains(text)

    def contains_tag(self, tag):
        return self.get_tags().contains(tag)

    def add_tags(self, tags):
        tags = [].extend(tags)
        self.get_tags().add_tags(tags)

    def __str__(self):
        str_ = f"{self.get_title()}, on {self.get_entry_time()} "
        str_ += f"with tags {self._tags}"
        return str_


class Note:
    def __init__(self, body, title):
        self._body = body
        self._title = title

    def get_body(self):
        return self._body

    def get_title(self):
        return self._title

    def contains(self, text):
        # TODO search by regex?
        return (text.lower() in self.get_title().lower()) or (
            text.lower() in self.get_body().lower()
        )

    def __le__(self, other):
        return self.get_title().lower() < other.get_title().lower()

    def __gt__(self, other):
        return self.get_title().lower() >= other.get_title().lower()

    def __str__(self):
        return self.get_title()
