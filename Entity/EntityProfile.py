from pydantic import BaseModel

class ProfileInsert(BaseModel):
    userId: int
    firstName: str

class ProfileDelete(BaseModel):
    id: int