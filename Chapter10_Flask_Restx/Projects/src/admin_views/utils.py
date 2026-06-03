from os import path
from uuid import uuid4

def generate_name(object, file):
    name, ext = path.splitext(file.filename)

    return f'{uuid4()}{ext}'