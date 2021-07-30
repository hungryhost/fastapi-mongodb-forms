import re


def is_email(value):
	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	if re.match(regex, value):
		return True
	return False


def is_phone(value):
	regex = r'([+]?\d{1})(\s)(\d{3}\s){2}\d{2}(\s)\d{2}'
	if re.match(regex, value):
		return True
	return False


def is_date(value):
	regex_1 = r'\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])'
	regex_2 = r'\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*'
	if re.match(regex_1, value) or re.match(regex_2, value):
		return True
	return False


