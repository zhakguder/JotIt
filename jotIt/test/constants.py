from jotIt.notes.note import NoteEntry, Note
from jotIt.notes.date import DateEntry
from jotIt.notes.tag import TagGroup
import datetime

BODY = "testing no way"
TITLE = "test contains nothing"
TAGS = ["a", "c", "b"]


today = datetime.date.today()
CURR_DATE = {"year": today.year, "month": today.month, "day": today.day}

LOW_DATE = {"year": today.year - 1, "month": 3, "day": 12}

HIGH_DATE = {"year": today.year + 1, "month": 4, "day": 12}


DATE_FORMAT = "%b %d %Y"


# TODO use mocks to get rid of these dependencies in tests

NOTE = Note(BODY, TITLE)
NOTE_DICT = {
    "date": {"date": "Oct 02 2010"},
    "note": {"body": "a", "title": "b"},
    "tags": {"tags": ["t1", "t2"]},
    # "note_id": 0,
    # "_id": ObjectId("5e459738cfc803fad62757d1"),
}
NOTE_ENTRY = NoteEntry([2020, 2, 11], [BODY, TITLE], TAGS)
DATE_ENTRY = DateEntry(*CURR_DATE.values())

TAGS_OBJECT = TagGroup(TAGS)
