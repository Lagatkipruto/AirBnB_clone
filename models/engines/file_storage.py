#!/usr/bin/python3
"""
FileStorage classmodel
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """deals with json files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets the id class name in objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serialize objs to json file"""
        with open(self.__file_path, mode="w") as f:
             dict_storage = {}
             for k, v in self.__objects.items():
                 dict_storage[k] = v.to_dict()
             json.dump(dict_storage, f)

    def reload(self):
        """deserializes json file to objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
