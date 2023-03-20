from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List
from legacyDB import db
from . import schema, services

router = APIRouter(tags=["StartingLaws"], prefix="/starting_laws")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_starting_law(
    request: schema.StartingLaw, database: Session = Depends(db.get_db)
):
    new_trait = await services.new_starting_law_register(request, database)
    return new_trait


@router.get("/", response_model=List[schema.DisplayStartingLaw])
async def get_all_starting_laws(
    database: Session = Depends(db.get_db),
):
    return await services.all_starting_laws(database)


@router.get("/{starting_law_id}", response_model=schema.DisplayStartingLaw)
async def get_starting_law_by_id(
    starting_law_id: int,
    database: Session = Depends(db.get_db),
):
    return await services.get_starting_law_by_id(starting_law_id, database)


@router.delete(
    "/{starting_law_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
async def delete_starting_law_by_id(
    starting_law_id: int,
    database: Session = Depends(db.get_db),
):
    return await services.delete_starting_law_by_id(starting_law_id, database)