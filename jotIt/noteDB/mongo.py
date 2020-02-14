import os
from pymongo import MongoClient

COLLECTION_NAME = "notes"


class MongoNoteDB:
    def __init__(self):
        mongo_url = os.environ.get("MONGO_URL")
        self.db = MongoClient(mongo_url).notes

    def find_all(self, selector):
        return self.db.notes.find(selector)

    def find(self, selector):
        return self.db.notes.find_one(selector)

    def create(self, note):
        return self.db.notes.insert_one(note)

    def update(self, selector, note):
        return self.db.notes.replace_one(selector, note).modified_count

    def delete(self, selector):
        return self.db.notes.delete_one(selector).deleted_count
