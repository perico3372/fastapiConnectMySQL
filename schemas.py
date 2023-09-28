#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# schemas.py
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    nombre: str
    rol: str
    estado: int
    
    class Config:
        orm_mode = True



