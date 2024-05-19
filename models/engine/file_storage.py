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
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dicts = {}
        for key, obj in FileStorage.__objects.items():
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(objects_dicts, f)

    def reload(self):
        objects_dict = {}
        with open(FileStorage.__file_path, 'r') as f:
            if os.path.getsize(FileStorage.__file_path) > 0:
                try:
                    objects_dict = json.load(f)
                    for k, v in objects_dict.items():
                        FileStorage.__objects[k] = v
                except FileNotFoundError:
                    pass
