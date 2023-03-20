from typing import List, Optional

from fastapi import HTTPException, status

from . import models
import datetime


async def new_user_register(request, database) -> models.User:
    current_time = datetime.datetime.now()
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password,
        created_at=current_time,
        updated_at=current_time,
        is_active=True,
        is_superuser=False)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database) -> List[models.User]:
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id, database) -> Optional[models.User]:
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    return user_info


async def delete_user_by_id(user_id, database):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
