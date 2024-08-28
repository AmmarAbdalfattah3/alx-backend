#!/usr/bin/env python3
"""bable flask module
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select the best match locale based on URL parameters,
       user settings, headers, or default locale.
    """

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    return request.accept_languages.best_match(
                app.config['LANGUAGES']
            ) or app.config['BABEL_DEFAULT_LOCALE']


def get_user():
    """Retrieve a user from the mock database
       based on login_as URL parameter.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set g.user to the current user based on login_as URL parameter."""
    g.user = get_user()


@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
