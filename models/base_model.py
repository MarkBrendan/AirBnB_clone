#!/usr/bin/python3
"""A Base class Module"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """my BaseModel class function """

    def __init__(self, *args, **kwargs):
       """constructor"""
       if kwargs is not None and kwargs != {}:
           for key in kwargs:
               if key == "created_at":self.__dict__["created_at"] = datetime.strptime(
                       kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
               elif key == "updated_at":
                   self.__dict__["updated_at"] = datetime.strptime(
                           kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
               else:
                   self.__dict__[key] = kwargs[key]
       else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with\
                the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of\
                __dict__ of the instance"""
        to_json = self.__dict__.copy()
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = self.created_at.isoformat()
        to_json['updated_at'] = self.updated_at.isoformat()
        return to_json
