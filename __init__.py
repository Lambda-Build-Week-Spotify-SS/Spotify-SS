"""Initializer - executes code when connecting from another file"""
from .app import create_app

APP = create_app()