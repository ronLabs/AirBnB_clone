#!/usr/bin/python3
"""class FileStorage"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import models


class FileStorage():
    """class for serialization"""
    __file_path = "file.json"
    __objects = {}
    __cls_name = {"User": User, "BaseModel": BaseModel, "Place": Place,
                  "State": State, "City": City, "Amenity": Amenity,
                  "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets objs in objs dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects in dictionary"""
        new_dict = {}
        for obj_id, obj in FileStorage.__objects.items():
            new_dict[obj_id] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file in dictionary"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dictss = json.load(f)
            for k, v in dictss.items():
                class_name = k.split(".")[0]
                if class_name in FileStorage.__cls_name:
                    self.__objects[k] = self.__cls_name[class_name](**v)
        except FileNotFoundError:
            pass
