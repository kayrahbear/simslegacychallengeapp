from pydantic import BaseModel, constr


class StartingLaw(BaseModel):
    name: constr(min_length=3, max_length=50)
    description: constr(min_length=3, max_length=255)
    law_type: constr(min_length=3, max_length=50)


class DisplayStartingLaw(StartingLaw):
    id: int
    name: str
    description: str
    law_type: str

    class Config:
        orm_mode = True
