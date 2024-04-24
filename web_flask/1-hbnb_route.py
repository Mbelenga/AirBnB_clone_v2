#!/usr/bin/python3
""" A script that starts the flask Web Application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Routing to root """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    The purpose of strict_slashes makes sure
    both versions of the URL (with and without trailing slashes)
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
