import datetime
import warnings
from unittest import TestCase, mock
from jotIt.test.constants import *
from jotIt.notes.schemas import NoteSchema, DateEntrySchema, TagsSchema, NoteEntrySchema

from marshmallow import pprint


class TestNoteSchema(TestCase):
    def test_note_schema(self):
        note_schema = NoteSchema()
        result = note_schema.dump(NOTE)
        self.assertEqual(result, NOTE.__dict__)
        note = note_schema.load(result)

    def test_date_schema(self):
        date_schema = DateEntrySchema()
        result = date_schema.dump(DATE_ENTRY)
        # How to format so they are equal
        pprint(result, indent=2)
        pprint(DATE_ENTRY.__dict__, indent=2)

    def test_tags_schema(self):
        tag_schema = TagsSchema()
        result = tag_schema.dump(TAGS_OBJECT)
        self.assertEqual(result, TAGS_OBJECT.__dict__)

    def test_note_entry_schema(self):
        note_entry_schema = NoteEntrySchema()
        result = note_entry_schema.dump(NOTE_ENTRY)
        # self.assertEqual(result, NOTE_ENTRY.__dict__)
