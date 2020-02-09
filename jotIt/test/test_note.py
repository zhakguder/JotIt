from unittest import TestCase
from jotIt import NoteEntry, Note
from jotIt.test.constants import *


class TestNote(TestCase):
    def test_note(self):
        note = Note(BODY, TITLE)
        self.assertEqual(note.get_body(), BODY)
        self.assertEqual(note.get_title(), TITLE)

    def test_note_entry(self):
        date = (YEAR, MONTH, DAY)
        message = (BODY, TITLE)
        note_entry = NoteEntry(date, message, TAGS)


if __name__ == "__main__":
    unittest.main()
