from jotIt.noteDB import Repository
from jotIt.noteDB.mongo import MongoNoteDB
from jotIt.notes.schemas import NoteEntrySchema
import json


class Service:
    note_id = 0

    def __init__(self, repo_client=Repository(adapter=MongoNoteDB)):
        self.repo_client = repo_client

    def find_all_notes(self, tag):
        notes = self.repo_client.find_all({"tags": tag})
        return [self.dump(note) for note in notes]

    def find_note(self, tag):
        note = self.repo_client.find({"tag": tag})
        return self.dump(note)

    def create_note_for(self, note):
        self.repo_client.create(self.prepare_note(note))
        return self.dump(note.data)

    # def update_note_with(self, tag, note):
    #     records_affected = self.repo_client.update({"tag": self.tag})

    def dump(self, data):
        return NoteEntrySchema().dump(data).data

    def prepare_note(self, note):
        # this might need to change
        data = note.__dict__
        # data = note.data
        data["note_id"] = Service.note_id
        Service.increase_note_id()
        return data

    @classmethod
    def increase_note_id(cls):
        cls.note_id += 1
