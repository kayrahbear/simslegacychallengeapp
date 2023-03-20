from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List
from legacyDB import db
from . import schema, services

router = APIRouter(tags=["Traits"], prefix="/trait")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_trait(
    request: schema.Trait, database: Session = Depends(db.get_db)
):
    new_trait = await services.new_trait_register(request, database)
    return new_trait


@router.get("/", response_model=List[schema.DisplayTrait])
async def get_all_traits(
    database: Session = Depends(db.get_db),
):
    return await services.all_traits(database)


@router.get("/{trait_id}", response_model=schema.DisplayTrait)
async def get_trait_by_id(
    trait_id: int,
    database: Session = Depends(db.get_db),
):
    return await services.get_trait_by_id(trait_id, database)


@router.delete(
    "/{trait_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
async def delete_trait_by_id(
    trait_id: int,
    database: Session = Depends(db.get_db),
):
    return await services.delete_trait_by_id(trait_id, database)