#!/usr/bin/python3
"""A script that starts a Flask web application
and has a route to hbnb"""
from flask import Flask

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hello_():
    """ Displays hbnb'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
