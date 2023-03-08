#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv

env_type = getenv("HBNB_TYPE_STORAGE")
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if env_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False,)
        places = relationship('Place', casacade='all, delete, delete-orphan', backref='cities')

    else:
        name = ''
        state_id = ''
