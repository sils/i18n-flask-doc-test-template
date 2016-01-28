"""
Contains the main Flask application.
"""

from os.path import dirname, abspath, join

from flask import Flask

current_path = dirname(__file__)
client_path = abspath(join(current_path, '..', 'client'))

app = Flask(__name__,
            static_url_path='',
            static_folder=client_path,
            template_folder=client_path)
app.config.from_object('server.config')
