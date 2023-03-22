from typing import List, Optional

from fastapi import HTTPException, status

from sqlalchemy import or_

from . import models


async def new_aspiration_register(request, database) -> models.Aspiration:
    new_aspiration = models.Aspiration(
        name=request.name,
        description=request.description,
        icon_url=request.icon_url,
        aspiration_type=request.aspiration_type,
    )
    database.add(new_aspiration)
    database.commit()
    database.refresh(new_aspiration)
    return new_aspiration


async def all_aspirations(database) -> List[models.Aspiration]:
    aspirations = database.query(models.Aspiration).all()
    return aspirations


async def all_child_aspirations(database) -> List[models.Aspiration]:
    child_aspirations = (
        database.query(models.Aspiration).filter(models.Aspiration.aspiration_type == "child").all()
    )
    return child_aspirations


async def all_teen_aspirations(database) -> List[models.Aspiration]:
    teen_aspirations = (
        database.query(models.Aspiration).filter(
            or_(models.Aspiration.aspiration_type == "teen+", models.Aspiration.aspiration_type == "teen")).all()
    )
    return teen_aspirations

async def all_adult_aspirations(database) -> List[models.Aspiration]:
    adult_aspirations = (
        database.query(models.Aspiration).filter(models.Aspiration.aspiration_type == "teen+").all()
    )
    return adult_aspirations



async def get_aspiration_by_id(aspiration_id, database) -> Optional[models.Aspiration]:
    aspiration_info = database.query(models.Aspiration).get(aspiration_id)
    if not aspiration_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !"
        )
    return aspiration_info


async def delete_aspiration_by_id(aspiration_id, database):
    database.query(models.Aspiration).filter(models.Aspiration.id == aspiration_id).delete()
    database.commit()
