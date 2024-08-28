#!/usr/bin/env python3
"""bable flask module
"""


from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    Determine the best match for the user's preferred language.

    This function is called by Flask-Babel to select the language to be used
    in the application, based on the Accept-Language header in the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Handle requests to the root URL ("/").

    Renders and returns the '2-index.html' template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    """
    Runs the Flask application if this script is executed directly.
    """
    app.run(debug=True)
