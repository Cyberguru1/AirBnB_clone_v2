#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
