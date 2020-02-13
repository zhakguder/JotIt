from jotIt.notes.note import NoteEntry, Note
from jotIt.notes.date import DateEntry
from jotIt.notes.tag import TagGroup

BODY = "testing no way"
TITLE = "test contains nothing"
TAGS = ["a", "c", "b"]


CURR_DATE = {"year": 2010, "month": 3, "day": 12}

LOW_DATE = {"year": 2009, "month": 3, "day": 12}

HIGH_DATE = {"year": 2010, "month": 4, "day": 12}


DATE_FORMAT = "%b %d %Y"


# TODO use mocks to get rid of these dependencies in tests

NOTE = Note(BODY, TITLE)
NOTE_ENTRY = NoteEntry([2020, 2, 11], [BODY, TITLE], TAGS)
DATE_ENTRY = DateEntry(*CURR_DATE.values())

TAGS_OBJECT = TagGroup(TAGS)
