#!/usr/bin/python3
"""
serves as the initialization file for the models package.
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User

storage = FileStorage()
storage.reload()
