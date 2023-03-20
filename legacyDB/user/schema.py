from pydantic import BaseModel, constr, validator, EmailStr
import datetime
from legacyDB import db
from . import models


class User(BaseModel):
    name: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8, max_length=255)
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_active: bool
    is_superuser: bool


class DisplayUser(User):
    id: int
    name: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
