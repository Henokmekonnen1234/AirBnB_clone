#!/usr/bin/python3
"""
Module city.py

This module have City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """This define about City class

    Attributes:
        state_id (State.id): id of State class instace
        name (str): the name of the city
    """
    state_id = ""
    name = ""
