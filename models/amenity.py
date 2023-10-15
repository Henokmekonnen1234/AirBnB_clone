#!/usr/bin/python3
"""
Module amenity.py

This module will define about Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class have public class instance name

    Attributes:
        name (str): holds the name of amenity
    """
    name = ""
