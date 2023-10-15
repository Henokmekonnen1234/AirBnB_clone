#!/usr/bin/python3
"""
Module review.py

This module contains Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class contain the public class instances

    Attributes:
        place_id (str): this will hold place id instance
        user_id (str): this will hold user id instace
        text (str): this contain users comment on the room
    """
    place_id = ""
    user_id = ""
    text = ""
