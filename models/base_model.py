#!/usr/bin/python3
"""Outlines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
from models.engine import file_storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
