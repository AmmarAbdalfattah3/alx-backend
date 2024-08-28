#!/usr/bin/env python3
"""flask module
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Handle requests to the root URL ("/").
    """
    return render_template('index.html')


if __name__ == '__main__':
    """
    The script will run the Flask development server if the script is
    executed directly (i.e., not imported as a module).
    """
    app.run(debug=True)
