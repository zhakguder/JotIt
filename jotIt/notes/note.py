from jotIt.notes.date import DateEntry
from jotIt.notes.tag import TagGroup


class NoteEntries:
    def __init__(self):
        self.entries = []

    def add_note(self, note):
        self.get_entries().append(note)

    def get_entries(self):
        return self._entries


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

    def get_note(self):
        return self._note

    def date_in_range(self, low_date, high_date):
        # low date and high date should be lists in format [Y, M, D]
        # TODO
        return self._date.is_in_range(low_date, high_date)

    def contains_text(self, text):
        return self.get_note().contains(text) or self.get_tags().contains(text)

    def contains_tag(self, tag):
        return self.get_tags().contains(tag)

    def add_tags(self, tags):
        tags = [].extend(tags)
        self.get_tags().add_tags(tags)


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

    def __leq__(self, other):
        return self.get_title().lower() <= other.get_title().lower()

    def __geq__(self, other):
        return self.get_title().lower() >= other.get_title().lower()
