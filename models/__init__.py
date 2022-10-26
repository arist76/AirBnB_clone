#!/usr/bin/env python3
"""
Contains models and related code
"""
from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
