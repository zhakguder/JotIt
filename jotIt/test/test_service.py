from unittest import TestCase, skip
from jotIt.service import Service
from jotIt.notes.note import NoteEntry
import json

service = Service()


def json_helper(inp):
    try:
        return inp.__dict__
    except:
        return inp.strftime("%b %d %Y")


class TestService(TestCase):
    # @skip("Skip till sometime")
    def test_create_note_for(self):
        note = NoteEntry([2010, 10, 2], ["a", "b"], ["t1", "t2"])

        note = json.loads(json.dumps(note, default=lambda o: json_helper(o)))
        res = service.create_note_for(note)

    def test_find_note(self):
        res = service.find_note("t1")
        self.assertNotEqual(res, [])

    def test_find_all_notes(self):
        res = service.find_all_notes("t1")
        self.assertNotEqual(res, [])


class JSONtoObjectDict(TestCase):
    pass
