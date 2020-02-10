from unittest import TestCase
from jotIt import NoteEntry, Note, NoteEntries
from jotIt.test.constants import *

YEAR = CURR_DATE["year"]
MONTH = CURR_DATE["month"]
DAY = CURR_DATE["day"]


class TestNote(TestCase):
    def setUp(self):
        self.note = Note(BODY, TITLE)

    def test_note(self):
        self.assertEqual(self.note.get_body(), BODY)
        self.assertEqual(self.note.get_title(), TITLE)

    def test_note_contains(self):
        self.assertTrue(self.note.contains("test"))
        self.assertFalse(self.note.contains("text"))


class TestNoteEntry(TestCase):
    def setUp(self):
        date = CURR_DATE.values()
        message = (BODY, TITLE)
        self.note_entry = NoteEntry(date, message, TAGS)

    def test_note_entry_contains_tag(self):
        self.assertTrue(self.note_entry.contains_tag(TAGS[0]))

    def test_note_entry_contains_text(self):
        self.assertTrue(self.note_entry.contains_text("test"))
        self.assertFalse(self.note_entry.contains_text("text"))

    def test_note_entry_add_tags(self):
        pass

    def test_note_entry_date_in_range(self):
        self.assertTrue(
            self.note_entry.date_in_range(LOW_DATE.values(), HIGH_DATE.values())
        )
        self.assertFalse(
            self.note_entry.date_in_range(HIGH_DATE.values(), LOW_DATE.values())
        )


class TestNoteEntries(TestCase):
    def setUp(self):
        ent1 = NoteEntry([2010, 1, 2], ["hello", "b"], "c")
        ent2 = NoteEntry([2009, 2, 4], ["yello", "a"], "c")
        ent3 = NoteEntry([2009, 1, 2], ["hello", "b"], "c")
        self.entries = NoteEntries()
        self.entries.add_note(ent1)
        self.entries.add_note(ent2)
        self.entries.add_note(ent3)

    def test_sort_entries(self):
        al = self.entries.sort_entries()
        sorted_titles = [entry.get_title() for entry in al]
        self.assertEqual(sorted_titles, ["a", "b", "b"])


if __name__ == "__main__":
    unittest.main()
