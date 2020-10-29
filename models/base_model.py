#!/usr/bin/python3
"""
Class Base
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    main class BaseModel to take cara of initialization, serialization,
    and deserializatoin of your future instances
    """
    def __init__(self, id, created_at, updated_at):
        """
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".format(self.__name__.__class__, self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
