from fastapi import APIRouter

from api.forms.routes import router

form_router = APIRouter()

form_router.include_router(router, tags=["forms"])