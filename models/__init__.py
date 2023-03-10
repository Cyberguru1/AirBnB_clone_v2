#!/usr/bin/python3
"""This module instantiates an object of class FileStorage and DBStorage
   depending on the type storage specified in the enviromental variable
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
