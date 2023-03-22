from typing import List, Optional

from fastapi import HTTPException, status

from sqlalchemy import or_

from . import models


async def new_trait_register(request, database) -> models.Trait:
    new_trait = models.Trait(
        name=request.name,
        description=request.description,
        icon_url=request.icon_url,
        trait_type=request.trait_type,
    )
    database.add(new_trait)
    database.commit()
    database.refresh(new_trait)
    return new_trait


async def all_traits(database) -> List[models.Trait]:
    traits = database.query(models.Trait).all()
    return traits


async def all_infant_traits(database) -> List[models.Trait]:
    infant_traits = (
        database.query(models.Trait).filter(models.Trait.trait_type == "infant").all()
    )
    return infant_traits


async def all_toddler_traits(database) -> List[models.Trait]:
    toddler_traits = (
        database.query(models.Trait).filter(models.Trait.trait_type == "toddler").all()
    )
    return toddler_traits

async def all_child_traits(database) -> List[models.Trait]:
    child_traits = (
        database.query(models.Trait).filter(models.Trait.trait_type == "child+").all()
    )
    return child_traits

async def all_teen_adult_traits(database) -> List[models.Trait]:
    teen_adult_traits = (
        database.query(models.Trait).filter(
            or_(models.Trait.trait_type == "child+", models.Trait.trait_type == "teen+")).all()
    )
    return teen_adult_traits

async def get_trait_by_id(trait_id, database) -> Optional[models.Trait]:
    trait_info = database.query(models.Trait).get(trait_id)
    if not trait_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !"
        )
    return trait_info


async def delete_trait_by_id(trait_id, database):
    database.query(models.Trait).filter(models.Trait.id == trait_id).delete()
    database.commit()
