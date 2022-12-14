import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fav_characters = relationship("Fav_characters", backref="user", lazy=True)
    fav_planets = relationship("Fav_planets", backref="user", lazy=True)

class Characters(Base):
    __tablename__ = 'characters'  
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    fav_characters = relationship("fav_characters", backref="user", lazy=True)
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
 

class Fav_characters(Base):
    __tablename__= "fav_characters"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    characters_id = Column(Integer, ForeignKey("characters.id"))


class Fav_planets(Base):
    __tablename__="fav_planets"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planets_id = Column(Integer, ForeignKey("planets.id"))
    


class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    fav_planets = relationship("fav_planets", backref="user", lazy=True)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
