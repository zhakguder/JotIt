from jotIt.notes.date import DateFactory


class NoteEntry:
    def __init__(self, date, message):
        # TODO: what is the format of date? (Y, M, D)
        # TODO: what is the format of message? (title, body)
        self._date = DateFactory.factory(*date)
        self._note = Note(*message)

    def get_entry_time(self):
        return self.date.getDate()

    def filter_date_in_range(self, low, high):
        # TODO
        pass

    def filter_contains_text(self, text):
        # TODO
        pass


class Note:
    def __init__(self, body, title):
        self._body = body
        self._title = title

    def get_body(self):
        return self._body

    def get_title(self):
        return self._title
