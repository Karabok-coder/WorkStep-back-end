from pydantic import BaseModel

class EntityOrder(BaseModel):
    nameWork: str
    timeStart: str
    timeEnd: str
    description: str
    salary: int
    city: str
    userAuthor: int
    timePublish: str
    category: str
    subcategory: str
    dateStart: str

class EntitySelectFilter(BaseModel):
    category: str
    subcategory: str
    city: str
    salaryStart: int
    salaryEnd: int
    dateStart: str
    dateEnd: str