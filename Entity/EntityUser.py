from pydantic import BaseModel

class EntityUser(BaseModel):
    email: str
    password: str
    nickname: str
    dateReg: str

class ExistUserEmail(BaseModel):
    email: str

class ExistUserNickname(BaseModel):
    nickname: str

class UpdateNicknameUser(BaseModel):
    nickname: str
    id: int

class UpdatePasswordUser(BaseModel):
    password: str
    id: int