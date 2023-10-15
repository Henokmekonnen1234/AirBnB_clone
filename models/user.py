#!/usr/bin/python3
"""
Module user.py

This module contain User datas
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class contain the user datas

    Attributes:
        email (str): holds email value
        password (str): holds password value
        first_name (str): holds first name
        last_name (str): holds last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
