from flask import Flask, json, g, request
from jotIt.service import Service as Note
from jotIt.notes.schemas import NoteEntrySchema
from flask_cors import CORS


# TODO add tests for this

app = Flask(__name__)
CORS(app)


@app.route("/notes", methods=["GET"])
def index(tag):
    return json_response(Note().find_all_notes(tag))


@app.route("/notes", methods=["POST"])
def create():
    note = NoteEntrySchema().load(json.loads(request.data))

    if note.errors:
        return json_response({"error": note.errors}, 422)
    note = Note().create_note_for(note)
    return json_response(note)


# TODO: delete note


def json_response(payload, status=200):
    return (json.dumps(payload), status, {"content-type": "application/json"})
