#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# models.py
from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "user"
        
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    
class Post(Base):
    __tablename__ = "post"
    #__table_args__ = {'extend_existing': True} #add
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    content = Column(String(200))
    user_id = Column(Integer)