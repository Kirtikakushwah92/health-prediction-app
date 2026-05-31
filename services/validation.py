import re
from datetime import date

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_dob(dob):
    return dob <= date.today()