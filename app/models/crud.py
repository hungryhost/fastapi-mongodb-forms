from bson.objectid import ObjectId
from database import get_collection
from schemas.form_schemas import form_schema_helper
import numpy as np


async def retrieve_forms():
    forms_collection = await get_collection()
    forms = []
    async for form in forms_collection.find():
        forms.append(form)
    return forms


# Add a new form into to the database
async def add_form(form_data: dict) -> dict:
    forms_collection = await get_collection()
    form = await forms_collection.insert_one(form_data)
    new_form = await forms_collection.find_one({"_id": form.inserted_id})
    return form_schema_helper(new_form)


# Retrieve a form with a matching ID
async def retrieve_form(id: str) -> dict:
    forms_collection = await get_collection()
    form = await forms_collection.find_ofine({"_id": ObjectId(id)})
    if form:
        return form_schema_helper(form)


async def retrieve_form_by_fields(fields: list) -> dict:
    forms_collection = await get_collection()
    #print(fields)
    values = []

    subquery = []
    for field in fields:
        subquery.append({field: {"$exists": True}})
    subquery = dict(zip(fields, values))
    query = {
        '$or': [subquery]
    }
    forms = {}
    async for form in forms_collection.find(query):
        forms[str(form['_id'])] = form
    print(forms)
    if forms:
        return forms


