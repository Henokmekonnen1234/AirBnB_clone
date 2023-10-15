#!/usr/bin/python3
"""
Module base_model.py

This module contains the basic fuction to convert file to dictionary,
json and revers it from json to class instances
"""

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """This class contains common attributes and methods for
        other classes
    """

    def __init__(self, *args, **kwargs):
        """this method will initialize the attributes

        Args:
            id (UUID): it's unique identifier for the object
            created_at (datetime):  assign with the current datetime
                                    when an instance is created
            update_at (datetime): it will be assigned when the object
                                    is changed
        """
        if len(kwargs) <= 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """returns the string representation of the class

        Returns:
            str: returns the string value
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method assignes the update_at instance with
        the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method will change class instances to dictionary

        Returns:
            dict: dictionary representation of the class instance
        """
        instance_dict = {}
        instance_dict['__class__'] = str(self.__class__.__name__)
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                instance_dict[key] = str(value.isoformat())
            else:
                instance_dict[key] = value
        return instance_dict
