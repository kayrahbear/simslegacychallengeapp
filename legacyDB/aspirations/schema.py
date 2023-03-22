from pydantic import BaseModel, constr
from typing import Optional


class Aspiration(BaseModel):
    name: constr(min_length=3, max_length=50)
    description: constr(min_length=3, max_length=350)
    icon_url: constr(min_length=3, max_length=50)
    aspiration_type: constr(min_length=3, max_length=50)


class DisplayAspiration(Aspiration):
    id: int
    name: str
    description: str
    icon_url: Optional[str]
    aspiration_type: str

    class Config:
        orm_mode = True
