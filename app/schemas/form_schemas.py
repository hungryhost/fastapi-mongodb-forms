from typing import Optional

from fastapi import Query
from pydantic import BaseModel, EmailStr, Field, validator
from pydantic.dataclasses import dataclass

ACCEPTABLE_TYPES = [
    'email',
    'text',
    'phone',
    'date',
]



def validate_field(cls, field_name_1):
    if field_name_1 not in ACCEPTABLE_TYPES:
        raise ValueError(f'Must be of acceptable type in {ACCEPTABLE_TYPES}')
    return field_name_1


def form_schema_helper(form) -> dict:
    return {
        "id": str(form["_id"]),
        "name": form["name"],
        "field_name_1": form["field_name_1"],
        "field_name_2": form["field_name_2"]
    }


class FormSchema(BaseModel):
    name: str
    field_name_1: str
    field_name_2: str

    _validate_field_name_1 = validator('field_name_1', allow_reuse=True)(validate_field)
    _validate_field_name_2 = validator('field_name_1', allow_reuse=True)(validate_field)


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}