#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
import datetime

class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    klass = value['__class__']
                    del value['__class__']
                    self.__objects[key] = eval(klass + '(**value)')
        except FileNotFoundError:
            pass
