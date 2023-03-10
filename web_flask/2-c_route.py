#!/usr/bin/python3
"""A script that starts a Flask web application
and has a route to hbnb"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_():
    """ Displays hbnb'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays hbnb'"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    """ Displays:
            returns text with C'"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
