from fastapi import APIRouter, status, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates("app/templates")

tabs = {"home":'active'}
@router.get(
    "/",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
def get_index(request: Request, hx_request: str | None = Header(default=None)):
    context = {
        "request": request,
        "hx_request":hx_request,
        "tabs": tabs
    }

    return templates.TemplateResponse("index.html", context)

@router.get(
    "/navbar",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
def get_navbar(request: Request, hx_request: str | None = Header(default=None)):
    context = {
        "request": request,
        "hx_request":hx_request,
        "tabs": tabs
    }

    return templates.TemplateResponse("nav.html", context)