"""
Contains the main Flask application.
"""

from os.path import abspath, dirname, join

from flask import Flask, request
from flask_babel import Babel

current_path = dirname(__file__)
client_path = abspath(join(current_path, '..', 'client'))

app = Flask(__name__,
            static_url_path='',
            static_folder=client_path,
            template_folder=client_path)
app.config.from_object('server.config')

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Called before the endpoints are queried to determine the best language from
    the request headers.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Start ignoring PyImportSortBear and PyLintBear (Those imports use app)

from . import index

# Stop ignoring
