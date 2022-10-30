#!/usr/bin/env python3
"""
Contains a FileStorage class that manages a models
persistency inside a json file
"""

import json
import os


class FileStorage:
    """ """

    __file_path = os.path.abspath("models.json")
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        appends the key <obj class name>.id to _objects
        with value obj
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serialized = {
            k: FileStorage.__objects[k].to_dict() for k in FileStorage.__objects.keys()
        }

        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized, json_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                loaded_dict = json.load(json_file)

                for k, v in loaded_dict.items():
                    cls_name = v["__class__"]
                    self.new(eval(cls_name)(**v))
        except FileNotFoundError:
            pass

    @property
    def file_path(self):
        return self.__file_path

    @property
    def get_object(self):
        return self.__objects
