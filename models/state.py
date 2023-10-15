#!/usr/bin/python3
"""
Module state.py

This module holds the value for State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class contain class instance of State class

    Attribute:
        name (str): will hold the name of state
    """
    name = ""
