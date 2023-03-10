from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session  # type: ignore
from typing import List

from app.auth.router import get_current_profile
from app import deps
from app import schemas
from app import models

from datetime import date
router = APIRouter()

from app import crud


@router.post(
    "",
    response_model=schemas.FoodLogProfile,
    status_code=status.HTTP_201_CREATED,
)
async def post_food_log(*, food_log: schemas.FoodLogCreate, db: Session = Depends(deps.get_db)):
    food_log_out = await crud.create(obj_in=food_log, db=db, model=models.Food_Log)
    return food_log_out

@router.get(
    "/date/{date}",
    response_model=schemas.DayLog,
    status_code=status.HTTP_200_OK,
)
async def get_food_log_date(*, date: date, profile: models.Profile = Depends(get_current_profile), db: Session = Depends(deps.get_db)) -> list[schemas.FoodLogProfile]:
    statement = select(models.Food_Log).where(models.Food_Log.profile_id == profile['id']).where(models.Food_Log.date == date)
    data = await db.execute(statement)
    test = data.unique().all()

    profile = await crud.read(_id=profile['id'], db=db, model=models.Profile)

    return {"profile":profile, "log":[value for value, in test]}

@router.get(
    "/{food_log_id}",
    response_model=schemas.FoodLogProfile,
    status_code=status.HTTP_200_OK,
)
async def get_food_log_id(*, food_log_id: int, db: Session = Depends(deps.get_db)):
    data = await crud.read(_id=food_log_id, db=db, model=models.Food_Log)
    if not data:
        raise HTTPException(status_code=404, detail="Food_log not found")
    return data

@router.get(
    "",
    response_model=List[schemas.FoodLog],
    status_code=status.HTTP_200_OK,
)
async def get_food_logs(*, profile: models.Profile = Depends(get_current_profile), db: Session = Depends(deps.get_db)):
    profile_id = profile['id']
    statement = select(models.Food_Log).where(models.Food_Log.profile_id == profile_id)
    data = await db.execute(statement)
    test = data.unique().all()

    return [value for value, in test]

@router.put(
    "/{food_log_id}",
    response_model=schemas.FoodLogProfile,
    status_code=status.HTTP_200_OK,
)
async def update_food_log(
    *, food_log_id: int, food_log_in: schemas.FoodLogBase, db: Session = Depends(deps.get_db)
):

    data = await get_food_log_id(food_log_id=food_log_id, db=db)

    data = await crud.update(db_obj=data, data_in=food_log_in, db=db)

    return data


@router.delete(
    "/{food_log_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_food_log(*, food_log_id: int, db: Session = Depends(deps.get_db)):
    data = await get_food_log_id(food_log_id=food_log_id, db=db)

    data = await crud.delete(_id=food_log_id, db=db, db_obj=data)
    return
