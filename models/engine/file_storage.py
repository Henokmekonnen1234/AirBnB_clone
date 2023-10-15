#!/usr/bin/python3
"""
Module file_storage.py

This code contains method usefull for file storage
"""

import importlib
import json


class FileStorage:
    """This class contains methods for serializing and deserializing
    objects to/from JSON.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): A dictionary to store objects with the
                          format <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary.

        Returns:
            dict: The dictionary containing stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary.

        Args:
            obj (object): An object to be stored.
        """
        if isinstance(type(obj), dict):
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj
        else:
            FileStorage.__objects = obj

    def save(self):
        """This methos will seriliaze the data and save it to sile
        """
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(self.obj_to_dict(FileStorage.__objects), json_file)

    def reload(self):
        """Deserializes the JSON file to populate the __objects dictionary."""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                file = json.load(json_file)
                FileStorage.__objects = self.dict_to_obj(file)
        except FileNotFoundError as e:
            print("Error not found", e)
        except Exception as e:
            print("other Exception", e)

    def obj_to_dict(self, objects):
        """This method will change class object to dictionary

        Args:
            objects (dict): dict contain class instaces

        Returns:
            dict: returs dictionary of class instaces
        """
        to_dict = {}
        for key in objects.keys():
            to_dict[key] = objects[key].to_dict()
        return to_dict

    def get_attribute(self, class_name):
        """it will create class instace

        Args:
            module (str): module name or file path
            class_name (str): class name

        Returns:
            obj: returns the class instance
        """
        base_model = importlib.import_module("models.base_model")
        user = importlib.import_module("models.user")
        if hasattr(base_model, class_name):
            return getattr(base_model, class_name)
        elif hasattr(user, class_name):
            return getattr(user, class_name)

    def dict_to_obj(self, dict_obj):
        """checks the class and will set the value

        Args:
            class_name (str): class name passed from file.json

        Retruns:
            dict: return dict and set it to private instace objects
        """
        to_obj = {}
        for key, value in dict_obj.items():
            class_new = self.get_attribute(value["__class__"])
            to_obj[key] = class_new(**value)
        return to_obj
