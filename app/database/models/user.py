import uuid
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    user_id: uuid.UUID = Field(primary_key=True)
    firstname: str
    secondname: str
    email: str
