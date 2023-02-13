from fastapi import APIRouter, Depends, status, Request, HTTPException, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session  # type: ignore
from app import deps
from app import schemas
from app import models
from datetime import date
from app.api.api_V1 import food_log as api_food_log
from app import crud

router = APIRouter()
templates = Jinja2Templates("app/templates")


@router.get(
    "/food_log",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
def get_create_log(*, request: Request, hx_request: str | None = Header(default=None), db: Session = Depends(deps.get_db)):
    print("test")
    context = {
            "request": request,
            "hx_request": hx_request,
            "tabs": {"food_log":"active"},
            "trigger": 'click'
        }

    return templates.TemplateResponse("create_food_log.html", context)

@router.get(
    "/serving_size",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
def get_create_serving(*, request: Request, hx_request: str | None = Header(default=None), db: Session = Depends(deps.get_db)):
    print("test")
    context = {
            "request": request,
            "hx_request": hx_request,
            "tabs": {"food":"active"},
            "trigger": 'click'
        }

    return templates.TemplateResponse("create_servings.html", context)

@router.get(
    "/food",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
def get_create_serving(*, request: Request, hx_request: str | None = Header(default=None), db: Session = Depends(deps.get_db)):
    print("test")
    context = {
            "request": request,
            "hx_request": hx_request,
            "tabs": {"food":"active"},
            "trigger": 'click'
        }

    return templates.TemplateResponse("create_food.html", context)