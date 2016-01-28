"""
Renders the index.html as a template.
"""
from flask.templating import render_template

from .app import app


@app.route('/')
@app.route('/index')
def index():
    r"""
    Renders the index.html as a template.
    """
    return render_template('index.html')
