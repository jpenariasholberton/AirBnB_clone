#!/usr/bin/python3
"""
Class Base
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Main class BaseModel to take cara of initialization, serialization,
    and deserializatoin of your future instances
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        if not bool(kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                                                    "%Y-%m-%dT%H:%M:%S.%f"))
                elif not key == "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        String representation of an object
        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of an instance
        """
        dic = {}
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
