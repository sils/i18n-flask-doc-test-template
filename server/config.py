"""
This file contains configuration options for the server side application.
"""

from os import environ

BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'
LANGUAGES = {'en'}

TESTING = environ.get("FLASK_TESTING") is not None
