#!/usr/bin/python3
"""
Module file_storage.py

This code contains method usefull for file storage
"""

import importlib
import json

class FileStorage:
    """This class contains methods for serializing and deserializing objects to/from JSON.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): A dictionary to store objects with the format <class name>.id.
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
        if type(obj) != dict:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj
        else:
            FileStorage.__objects = obj

    def save(self):
        """Serializes __objects to a JSON file."""
        for key in FileStorage.__objects.keys():
            if hasattr(FileStorage.__objects[key], "to_dict"):
                FileStorage.__objects[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """Deserializes the JSON file to populate the __objects dictionary."""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                file = json.load(json_file)
                for key, value in file.items():
                    module = importlib.import_module("models.base_model")
                    class_obj = getattr(module, value["__class__"])
                    FileStorage.__objects[key] = class_obj(**value)
        except FileNotFoundError as e:
            print("Error not found", e)
        except Exception as e:
            print("other Exception", e)
