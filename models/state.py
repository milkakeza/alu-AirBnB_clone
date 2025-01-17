#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a State instance

        Args:
            *args (list): List of arguments
            **kwargs (dict): Dictionary of keyword arguments
        """
        super().__init__(*args, **kwargs)
