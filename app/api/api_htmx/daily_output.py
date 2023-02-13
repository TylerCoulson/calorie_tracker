from fastapi import APIRouter, Depends, status, Request, HTTPException, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session  # type: ignore
from datetime import date
from app import deps
from app import schemas
from app import models

from app.api.calcs.calcs import resting_rate, age
from app.api.calcs import calorie_calcs
from app.api.api_V1 import daily_output as api_daily

router = APIRouter()
templates = Jinja2Templates("app/templates")

from app import crud


# @router.post(
#     "",
#     response_model=schemas.DailyOutputBase,
#     status_code=status.HTTP_201_CREATED,
# )
# def post_daily(*, actual_weight: schemas.DailyOutputInput, db: Session = Depends(deps.get_db)):
    
#     log = crud.create(obj_in=actual_weight, db=db, model=models.DailyLog)
    
#     output_data = daily_log(user_id=log.user_id, date=log.date, db=db)
#     return output_data


@router.get(
    "",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
def get_daily(*, request: Request,hx_request: str | None = Header(default=None), user_id:int, date:date = date.today(), db: Session = Depends(deps.get_db)):
    output_data = jsonable_encoder(api_daily.get_daily(user_id=user_id, date=date, db=db))
    
    context = {
                "request": request,
                "hx_request": hx_request,
                "daily": output_data
            }
    return templates.TemplateResponse("daily.html", context)
    