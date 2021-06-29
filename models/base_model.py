#!/usr/bin/python3
"""class BaseModel"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """definition class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes method"""
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    setattr(self, k, datetime.strptime(v, tformat))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

    def __str__(self):
        """return format string"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
