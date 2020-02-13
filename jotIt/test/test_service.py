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
        print(note.__dict__)

        # why? This was working prior
        import pdb

        pdb.set_trace()
        note = json.dumps(note, lambda o: json_helper(o))

        # service.create_note_for(note)
