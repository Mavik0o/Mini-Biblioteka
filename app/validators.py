import re

from app.exceptions import InvalidEmailError


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise InvalidEmailError("Nieprawidłowy adres email.")

    return True