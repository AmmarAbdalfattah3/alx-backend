#!/usr/bin/env python3
"""babel flask module
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class to store configuration variables for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def index():
    """
    Handle requests to the root URL ("/").

    Renders and returns the '1-index.html' template.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    """
    Runs the Flask application if this script is executed directly.
    """
    app.run(debug=True)
