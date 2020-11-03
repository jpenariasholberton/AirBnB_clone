#!/usr/bin/python3
"""
Class FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    The class FileStorage serializes instances to a JSON
    file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}
    name_class = {'BaseModel': BaseModel,
                  'User': User, 'State': State,
                  'City': City, 'Place': Place,
                  'Amenity': Amenity, 'Review': Review}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Method sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        dic = {}
        for key, value in self.__objects.items():
            if isinstance(value, BaseModel):
                dic[key] = value.to_dict()
            else:
                dic[key] = value
            # dic[key] = value.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(dic, json_file)

    def reload(self):
        """
        Method deserializes the JSON file to __objects
        """
        new = {}
        try:
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                new = json.load(json_file)
                for key, value in new.items():
                    self.__objects[key] = self.name_class[value["__class__"]](
                        **value)
        except:
            pass
