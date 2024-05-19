#!/usr/bin/python3
""" class file_storage module"""
import json
import os


class FileStorage:
    """ file_storage function"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key:obj})

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dicts = {}

        with open(self.__file_path, mode='w', encoding='utf-8') as f:

            for k, v in self.__objects.items():
                objects_dicts[k] = v.to_dict()
            json.dump(objects_dicts, f)

    def classes(self, obj_name, dicts):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}

        for k in classes:
            if (obj_name == k):
                new_obj = classes[k](**dicts)
        return new_obj


    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                objects_dict = json.load(f)

            for k in objects_dict:
                obj_id = k.split(".")[0]
                new_objs = self.classes(obj_id, objects_dict[key])
                if new_objs is not None:
                    self.__objects[k] = new_objs
        except FileNotFoundError:
            pass
