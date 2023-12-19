#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, String, Integer, Column
from sqlalchemy.orm import relationship
from sqlalchemy import Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(128))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0) 
    max_guest =  Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude =  Column(Float, nullable=False, default=0)
    longitude =  Column(Float, nullable=False, default=0)
    amenity_ids = []

    # table realationships

    cities = relationship("City", back_populates='places')
    users = relationship("User", back_populates='places')
