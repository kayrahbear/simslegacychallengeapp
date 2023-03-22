from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List
from legacyDB import db
from . import schema, services

router = APIRouter(tags=["Aspirations"], prefix="/aspiration")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_aspiration(
        request: schema.Aspiration, database: Session = Depends(db.get_db)
):
    new_aspiration = await services.new_aspiration_register(request, database)
    return new_aspiration


@router.get("/", response_model=List[schema.DisplayAspiration])
async def get_all_aspirations(
        database: Session = Depends(db.get_db),
):
    return await services.all_aspirations(database)


@router.get("/child", response_model=List[schema.DisplayAspiration])
async def get_all_child_aspirations(
        database: Session = Depends(db.get_db),
):
    return await services.all_child_aspirations(database)


@router.get("/teen", response_model=List[schema.DisplayAspiration])
async def get_all_teen_aspirations(
        database: Session = Depends(db.get_db),
):
    return await services.all_teen_aspirations(database)


@router.get("/adult", response_model=List[schema.DisplayAspiration])
async def get_all_adult_aspirations(
        database: Session = Depends(db.get_db),
):
    return await services.all_adult_aspirations(database)


@router.get("/{aspiration_id}", response_model=schema.DisplayAspiration)
async def get_aspiration_by_id(
        aspiration_id: int,
        database: Session = Depends(db.get_db),
):
    return await services.get_aspiration_by_id(aspiration_id, database)


@router.delete(
    "/{aspiration_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
async def delete_aspiration_by_id(
        aspiration_id: int,
        database: Session = Depends(db.get_db),
):
    return await services.delete_aspiration_by_id(aspiration_id, database)
