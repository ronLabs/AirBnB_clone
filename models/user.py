#!/usr/bin/python3
"""create class User """
from models.base_model import BaseModel


class User(BaseModel):
    """init class User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
