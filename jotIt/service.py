import json
from abc import ABC, abstractmethod
from jotIt.noteDB import Repository
from jotIt.noteDB.mongo import MongoNoteDB
from jotIt.notes.schemas import NoteEntrySchema
from jotIt.notes.note import NoteEntry
from jotIt.notes.date import Date


class Service:
    note_id = 0

    def __init__(self, note_client=Repository(adapter=MongoNoteDB)):
        self.note_client = note_client.client

    def find_all_notes(self, tag):
        notes = self.note_client.find_all({"tags.tags": tag})
        return [self.dump(note) for note in notes]

    def find_note(self, tag):

        note = self.note_client.find({"tags.tags": tag})
        return self.dump(note)

    def create_note_for(self, note):
        self.note_client.create(self.prepare_note(note))

        return self.dump(note)

    # def update_note_with(self, tag, note):
    #     records_affected = self.repo_client.update({"tag": self.tag})

    def dump(self, data):
        # TODO check NoteEntrySchema(exclude=['note_id']) doesn't exclude note_id
        # TODO also, this approach is not clean, possibly there is a better way to do this

        data = JSONtoObjectDict.convert(data)

        # TODO will this always be of NoteEntry class?
        note = NoteEntry(*data)
        return NoteEntrySchema().dump(note)

    def prepare_note(self, note):
        # TODO
        # this might need to change
        data = note
        # data = note.data
        data["note_id"] = Service.note_id
        Service.increase_note_id()
        return data

    @classmethod
    def increase_note_id(cls):
        cls.note_id += 1


class JSONtoObjectDict:
    @staticmethod
    def convert(data):
        data = JSONtoObjectDict.clean_dict(data)
        converter = JSONtoObjectDict.create_converter(data)
        data = converter.convert(data)
        return data

    @staticmethod
    def create_converter(data):
        # TODO clean this up
        converter_class = None
        for key, value in data.items():

            if key in ["note", "date", "tags"]:
                for k, v in value.items():
                    if k == "date" and type(v) == str:
                        converter_class = JSONtoObjectInfo
        return converter_class

    @staticmethod
    def clean_dict(data, keys_to_remove=["note_id", "_id"]):
        for key in keys_to_remove:
            del data[key]
        return data


class JSONtoObjectInfo:
    @staticmethod
    def convert(data):

        for key, value in data.items():
            if key == "date":
                date = Date.date_str_to_date_object(value["date"])
                year = date.year
                month = date.month
                day = date.day
                date_component = [year, month, day]
            elif key == "note":
                note_component = list(value.values())
            elif key == "tags":

                tags_component = list(value.values())[0]
        return [date_component, note_component, tags_component]
