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
        """Serialize __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, 'w') as f:
            objects_dicts = {}
            for key, obj in FileStorage.__objects.items():
                json.dump(objects_dicts, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects_dict = json.load(f)
                for key, obj_dic in objects_dict.items():
                    obj = BaseModel(**obj_dic)
                    FileStorage.__objects[key] = obj
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
