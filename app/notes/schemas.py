from pydantic import BaseModel, ConfigDict

# Shared Base Fields
class NoteBase(BaseModel):
    title:str
    content:str

#  For Creation
class NoteCreate(NoteBase):
    pass

# For Partial Update
class NotePatch(BaseModel):
    title:str | None = None
    content:str | None = None

# For Update
class NoteUpdate(BaseModel):
    title:str
    content:str 

# For Delete
class NoteOut(NoteBase):
    id:int
    model_config = ConfigDict(from_attributes=True)