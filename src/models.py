import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}
class User(Base):
    __tablename__ = 'user'
    customer_id = Column(Integer, primary_key=True)
    first_Name = Column(String(20), index=True) 
    last_Name = Column(String(20))
    password = Column(String(30))

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user1.customer_id'))
    user_to_id = Column(Integer, ForeignKey('user2.customer_id'))
    user1 = relationship(User)
    user2 = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey('post.customer_id'))
    post = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('comments.customer_id'))
    comments = relationship(User)
    post_id = Column(Integer, ForeignKey('comments2.id'))
    comments2 = relationship (Post)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
