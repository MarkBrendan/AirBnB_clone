#!/usr/bin/python3
"""A Base class Module"""

import uuid
import datetime
from models import storage


class BaseModel:
    """my BaseModel class function """

    def __init__(self, *args, **kwargs):
        """constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in [self.created_at, self.updated_at]:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_to = self.__dict__.copy()
        dict_to['__class__'] = self.__class__.__name__
        if self.created_at in dict_to:
            dict_to['created_at'] = self.created_at.isoformat()
        if self.updated_at in dict_to:
            dict_to['updated_at'] = self.updated_at.isoformat()
        return dict_to
