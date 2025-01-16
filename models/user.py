#!/usr/bin/python3

from models.base_model import BaseModel

class User:
    """
    User class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a User instance
        """

        super().__init__(*args, **kwargs)