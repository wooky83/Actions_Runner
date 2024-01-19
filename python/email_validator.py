import re

def is_valid_email(email):  
    match = re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)  
    if not bool(match):   
        return False  
    return True