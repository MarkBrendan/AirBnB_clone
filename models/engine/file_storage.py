#!/usr/bin/python3
""" class file_storage module"""
import json

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
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                value = json.load(file)
                for key, obj in value.items():
                    FileStorage.__file_path[key] = obj
        except FileNotFoundError:
            pass
