from datetime import date

from pydantic import BaseModel


class UsersSchema(BaseModel):
    user_id: int
    username: str
    password: str
    email: str
    registration_date: date
    user_type: str

    class Config:
        from_orm = True
        from_attributes = True


class UserCreateSchema(BaseModel):
    username: str
    password: str
    email: str
    user_type: str
