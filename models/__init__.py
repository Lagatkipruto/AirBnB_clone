#!/usr/bin/python3
""" This is the initialization file"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
