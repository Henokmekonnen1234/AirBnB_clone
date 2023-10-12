#!/usr/bin/python3
"""
Module __init__.py

This module will call the FileStorage class
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
