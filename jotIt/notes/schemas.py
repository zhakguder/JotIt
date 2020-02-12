from marshmallow import Schema, fields, post_load
from jotIt.notes.note import Note, NoteEntry
from jotIt.notes.date import DateEntry
from jotIt.notes.tag import TagGroup


class NoteSchema(Schema):
    body = fields.Str()
    title = fields.Str()

    @post_load
    def make_note(self, data, **kwargs):
        return Note(**data)


class DateEntrySchema(Schema):
    date = fields.Date()

    @post_load
    def make_date(self, data, **kwargs):
        return DateEntry(**data)


class TagsSchema(Schema):
    tags = fields.List(fields.Str())

    @post_load
    def make_tags(self, data, **kwargs):
        return TagGroup(**data)


class NoteEntrySchema(Schema):
    date = fields.Nested(DateEntrySchema())
    note = fields.Nested(NoteSchema())
    tags = fields.Nested(TagsSchema())
