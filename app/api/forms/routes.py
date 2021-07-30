from fastapi import APIRouter, Depends, HTTPException, Body, Request
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from .forms_controller import get_form_by_fields, evaluate_types
from models.crud import add_form
from schemas.form_schemas import FormSchema, ResponseModel
router = APIRouter()


@router.post(
    path="/get_form",
    status_code=200
)
async def get_form(request: Request):
    #print(list(request.query_params.keys()))
    form = await get_form_by_fields(
        requested=dict(request.query_params)
    )
    if form is None:
        types = evaluate_types(
            requested=dict(request.query_params)
        )
        return types
    else:
        return {"name": form['name'], "form_data_debug": str(form)}

