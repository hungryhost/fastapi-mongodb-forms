from typing import Union

from models.crud import retrieve_form_by_fields, retrieve_forms
from .validators import is_email, is_date, is_phone
import operator


async def get_form_by_fields(requested: dict) -> Union[None, dict]:
	forms = await retrieve_form_by_fields(list(requested.keys()))
	multiple_forms = await retrieve_forms()
	print(multiple_forms)
	if not forms:
		return None
	evaluated_forms = {}
	evaluated_forms_1 = {}

	# this loop is used to evaluate which form suits best in terms of attributes

	for form in forms.values():
		evaluated_forms[str(form['_id'])] = len(list(set(form.keys()) - set(requested.keys())))
	#print(evaluated_forms)
	best_form = min(evaluated_forms, key=evaluated_forms.get)

	form = forms[best_form]
	form_with_data = {}
	form_to_process = form.copy()
	form.pop('_id')
	form.pop('name')

	for key, value in form.items():
		try:
			form_with_data[value] = requested[key]
		except Exception as e:
			pass
	val_validation = False
	for key, value in form_with_data.items():
		if key == 'email':
			val_validation = is_email(value)
			#print(val_validation)
		if key == 'phone':
			val_validation = is_phone(value)
			#print(value)
			#print(val_validation)
		if key == 'date':
			val_validation = is_date(value)
			#print(val_validation)
		if not val_validation:
			return None
	if val_validation:
		return form_to_process

	return None


def evaluate_types(requested: dict) -> dict:
	return_dict = {}
	for key, value in requested.items():
		if is_date(value):
			return_dict[key] = 'date'
			continue
		if is_email(value):
			return_dict[key] = 'email'
			continue
		if is_phone(value):
			return_dict[key] = 'phone'
			continue
		return_dict[key] = 'text'
	return return_dict
