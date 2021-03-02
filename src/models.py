import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People_Fav(Base):
    __tablename__ = 'people_fav'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }
    
class Planet_Fav(Base):
    __tablename__ = 'planet_fav'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

class People(Base):
    __tablename__ = 'people'
    
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Date)
    gender = Column(String)
    birth_year = Column(Date)
    created = Column(Date)
    edited = Column(Date)
    name = Column(String)
    homeworld = Column(String)
    url = Column(String)
    description = Column(String)
    photo = Column(String)
    liked_by_users = relationship("People_Fav", backref="people")

    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "created": self.created,
            "edited": self.edited,
            "name": self.name,
            "homeworld": self.homeworld,
            "url": self.url,
            "description": self.description,
            "photo": self.photo
        }

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    created = Column(Date)
    edited = Column(Date)
    name = Column(String) 
    url = Column(String)
    description = Column(String)
    photo = Column(String)
    liked_by_users = relationship("Planet_Fav", backref="planet")

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
            "name": self.name,
            "url": self.url,
            "description": self.description,
            "photo": self.photo,
        }

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    profile_photo = Column(String(250))
    favourite_planets = relationship("Planet_Fav", backref="user")
    favourite_people = relationship("People_Fav", backref="user")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "profile_photo": self.profile_photo
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')