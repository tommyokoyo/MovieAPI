#!/usr/bin/env python3
"""
    Base Module
"""
from datetime import datetime
from typing import TypeVar, List, Iterable
from os import path
import json
import uuid

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATA = {}


class Base:
    """
        Model Class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
            Initializes base instance class
            :param args: List
            :param kwargs: Dict
        """
        obj_class = str(self.__class__.__name__)

        if DATA.get(obj_class) is None:
            DATA[obj_class] = {}

        self.id = kwargs.get('id', str(uuid.uuid4()))

        if kwargs.get('created_at') is not None:
            self.created_at = datetime.strptime(kwargs.get('created_at'), TIMESTAMP_FORMAT)
        else:
            self.created_at = datetime.utcnow()

        if kwargs.get('updated_at') is not None:
            self.updated_at = datetime.strptime(kwargs.get('updated_at'), TIMESTAMP_FORMAT)
        else:
            self.updated_at = datetime.utcnow()

    def __eq__(self, other: TypeVar('Base')) -> bool:
        """
            Equality
            :param other:
            :return:
        """
        if type(self) != type(other):
            return False
        if not isinstance(self, Base):
            return False
        return (self.id == other.id)

    def to_json(self, for_serialization: bool = False) -> dict:
        """
            Convert the object to a JSON dictionary
            :param for_serialization:
            :return: Dict
        """
        result = {}

        for key, value in self.__dict__.items():
            if not for_serialization and key[0] == '_':
                continue
            if type(value) is datetime:
                result[key] = value.strftime(TIMESTAMP_FORMAT)
            else:
                result[key] = value

        return result

    @classmethod
    def load_from_file(cls):
        """
            Loads all objects from file
            :return:
        """
        obj_class = cls.__name__
        file_path = f'db_{obj_class}.json'
        DATA[obj_class] = {}
        if not path.exists(file_path):
            return None

        with open(file_path, 'r') as f:
            json_obj = json.load(f)
            for obj_id, obj_json in json_obj.items():
                DATA[obj_class][obj_id] = cls(**obj_json)

    @classmethod
    def save_to_file(cls):
        """
            Saves all objects to a file
            :return:
        """
        obj_class = cls.__name__
        file_path = f'db_{obj_class}.json'
        objs_json = {}

        if path.exists(file_path):
            with open(file_path, 'r') as f:
                objs_json = json.load(f)

        for obj_id, obj in DATA[obj_class].items():
            objs_json[obj_id] = obj.to_json(True)

        with open(file_path, 'w') as f:
            json.dump(objs_json, f)

    def save(self):
        """
            Save current object
            :return:
        """
        obj_class = self.__class__.__name__
        self.updated_at = datetime.utcnow()
        DATA[obj_class][self.id] = self
        self.__class__.save_to_file()

    def remove(self):
        """
            Remove/Delete an object
            :return:
        """
        obj_class = self.__class__.__name__
        if DATA[obj_class].get(self.id) is not None:
            del DATA[obj_class][self.id]
            self.__class__.save_to_file()

    @classmethod
    def search(cls, attributes: dict = {}) -> List[TypeVar('Base')]:
        """
            Search all objects with matching attributes
            :return:
        """
        obj_class = cls.__name__
        def _search(obj):
            if len(attributes) == 0:
                return True
            for k, v in attributes.items():
                if getattr(obj, k) != v:
                    return False

            return True

        return list(filter(_search, DATA[obj_class].values()))

    @classmethod
    def get(cls, obj_id: str) -> TypeVar('Base'):
        """
            Returns on object by id
            :param obj_id:
            :return:
        """
        obj_class = cls.__name__
        return DATA[obj_class].get(obj_id)

    @classmethod
    def all(cls) -> Iterable[TypeVar('Base')]:
        """
            Returns all objects
            :return:
        """
        return cls.search()
