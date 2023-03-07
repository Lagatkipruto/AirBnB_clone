#!/usr/bin/python3
"""This is he base model for the Airbnb clone project"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """this is the baseclass for the project"""

    def __init__(self, *args, **kwargs):
        """The initializing method"""

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime(now)
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformayt(value))
                    else:
                        setattr(self, key, value)
    def __str__(self):
        """Returns the string representation of the basemodel object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary representation containing all the keys/values"""
          dict_1 = self.__dict__.copy()
          dict_1["__class__"] = self.__class__.__name__
          for k, v in self.__dict__.items():
              if k in ("created_at", "updated_at"):
                  v = self.__dict__[k].isoformat()
                  dict_1[k] = v
                  return dict_1
