from marshmallow import Schema, fields


class NoteSchema(Schema):
    _body = fields.Str()
    _title = fields.Str()


class DateEntrySchema(Schema):
    _date = fields.Date()


class TagsSchema(Schema):
    _tags = fields.List(fields.Str())


class NoteEntrySchema(Schema):
    _date = fields.Nested(DateEntrySchema())
    _note = fields.Nested(NoteSchema())
    _tags = fields.Nested(TagsSchema())
