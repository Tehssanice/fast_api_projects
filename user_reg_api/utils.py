import re


def is_valid_username(username):
    return bool(re.match("^[a-zA-Z0-9_]+$", username))


def is_valid_password(password):
    return bool(re.search("[a-z]", password)) and bool(re.search("[A-Z]", password)) and bool(re.search("[0-9]", password))
