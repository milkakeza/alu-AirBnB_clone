#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
JSON module
"""

from models.base_model import BaseModel
"""
BaseModel class import
"""
class FileStorage:
    """
    Class FileStorage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):

        """
        Returns a dictionary of all the objects stored in __objects
        """
        return FileStorage.__objects

    def new(self, obj):

        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (Object): The object to be stored
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file __file_path
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

            try:
                with open(self.__file_path, "w") as f:
                    json.dump(obj_dict, f, indent=4)
            except FileNotFoundError:
                pass

    def reload(self):
        """
        Deserializes the JSON file __file_path to __objects, if it exists

        If the file does not exist, no exception is raised
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
        