from pydantic import BaseModel, constr
from typing import Optional


class Trait(BaseModel):
    name: constr(min_length=3, max_length=50)
    description: constr(min_length=3, max_length=350)
    icon_url: constr(min_length=3, max_length=50)
    trait_type: constr(min_length=3, max_length=50)


class DisplayTrait(Trait):
    id: int
    name: str
    description: str
    icon_url: Optional[str]
    trait_type: str

    class Config:
        orm_mode = True
