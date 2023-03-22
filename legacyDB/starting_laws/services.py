from typing import List, Optional

from fastapi import HTTPException, status

from . import models
import datetime


async def new_starting_law_register(request, database) -> models.StartingLaw:
    new_law = models.StartingLaw(
        name=request.name,
        description=request.description,
        law_type=request.law_type,
    )
    database.add(new_law)
    database.commit()
    database.refresh(new_law)
    return new_law


async def all_starting_laws(database) -> List[models.StartingLaw]:
    starting_laws = database.query(models.StartingLaw).all()
    return starting_laws


async def all_gender_starting_laws(database) -> List[models.StartingLaw]:
    gender_starting_laws = (
        database.query(models.StartingLaw).filter(models.StartingLaw.law_type == "gender").all()
    )
    return gender_starting_laws


async def all_bloodline_starting_laws(database) -> List[models.StartingLaw]:
    bloodline_starting_laws = (
        database.query(models.StartingLaw).filter(models.StartingLaw.law_type == "bloodline").all()
    )
    return bloodline_starting_laws


async def all_heir_starting_laws(database) -> List[models.StartingLaw]:
    heir_starting_laws = (
        database.query(models.StartingLaw).filter(models.StartingLaw.law_type == "heir").all()
    )
    return heir_starting_laws


async def all_species_starting_laws(database) -> List[models.StartingLaw]:
    species_starting_laws = (
        database.query(models.StartingLaw).filter(models.StartingLaw.law_type == "species").all()
    )
    return species_starting_laws


async def get_starting_law_by_id(starting_law_id, database) -> Optional[models.StartingLaw]:
    starting_law_info = database.query(models.StartingLaw).get(starting_law_id)
    if not starting_law_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !"
        )
    return starting_law_info


async def delete_starting_law_by_id(starting_law_id, database):
    database.query(models.StartingLaw).filter(models.StartingLaw.id == starting_law_id).delete()
    database.commit()
