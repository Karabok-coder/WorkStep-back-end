from pydantic import BaseModel

class Email(BaseModel):
    seed: int
    username: str
    email: str