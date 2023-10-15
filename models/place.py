#!/usr/bin/python3
"""
Module place.py

This module contains instances of Place class
"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City


class Place(BaseModel):
    """This class contain public class instaces of Place

    Attributes:
        city_id (str): contain id of city
        user_id (str): contain is of user
        name (str): contain name of place
        desciption (str): contain detail of place
        number_rooms (int): contain number of rooms in that place
        number_bathrooms (int): contain number of bathrooms
        max_guest (int): how many maximum guest can take
        price_by_night (int): contain price of the room for each night
        lattitude (float): contain geographical lattitude
        longitude (float): contain geographical longitude
        amenity_ids (list): list of Amenity.id values
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latittude = 0.0
    longitude = 0.0
    amenity_ids = []
