#!/usr/bin/python3
"""
Module city.py

This module have City class
"""

from models.base_module import BaseModel
from models.state import State


class City(BaseModel, State):
    """This define about City class

    Attributes:
        state_id (State.id): id of State class instace
        name (str): the name of the city
    """
    state_id = State.id
    name = ""
