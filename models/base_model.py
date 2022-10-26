#!/usr/bin/env python3
"""
Contains an abstract model
"""
import datetime
import uuid
from .__init__ import storage


class BaseModel:
    """
    An abstract model interface

    a model to be inherited by concrete sub models

    Attributes
    ----------
    id : str
        unique uuid string format generated by uuid.uuid4()

    created_at : datetime.datetime
        the datetime the object is created at

    updated_at : datetime.datetime
        the datetime the object is updated at, if the object is never updated
        this will be the same as created_at

    Methods
    -------
    save()
        changes updated_at to datetime.datetime.now()

    to_dict()
        returns deserialized __dict__ with added keys like __class__
    """

    def __init__(self, *args, **kwargs):
        """
        if kwargs is not empty it serializes kwargs to a Model object
        else creates new object

        Parameters
        ---------
        args
            not used here

        kwargs
            dict to serialize
        """
        if kwargs:
            for k in kwargs.keys():
                v = None
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    v = datetime.datetime.fromisoformat(kwargs[k])
                else:
                    v = kwargs[k]

                self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        formats the str of the object

        Returns
        -------
        a string formated as '[self.__class__.__name__] (self.id) self.__dict__
        e.g. [Basemodel] (bd19004e-3ca3-4b27-963a-0f986b967479) {}
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        First updates updated_at to datetime.datetime.now()
        then saves the instance to storage
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Deserializes the object to a python dictionary with the datetime
        changed to isoformat

        Returns
        -------
        a dict with all the instance attribute plus the class name with
        key __class__
        """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = d["created_at"].isoformat()
        d["updated_at"] = d["updated_at"].isoformat()

        return d
