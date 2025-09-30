from fastapi import FastAPI
from app.notes import services as notes_services

app = FastAPI()

@app.post("/notes")
async def note_create(new_note:dict):
    note = await notes_services.create_note(new_note["title"], new_note["content"])
    return note

@app.get("/notes/{note_id}")
async def note_get(note_id:int):
    note = await notes_services.get_note(note_id)
    return note