#!/usr/bin/python3
"""class FileStorage"""

from models.base_model import BaseModel
import json
import models


class FileStorage():
    """class for serialization"""
    __file_path = "file.json"
    __objects = {}

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
                FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            pass
