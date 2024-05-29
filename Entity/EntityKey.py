from pydantic import BaseModel

class EntityKey(BaseModel):
    userId: int