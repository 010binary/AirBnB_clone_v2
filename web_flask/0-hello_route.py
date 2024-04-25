#!/usr/bin/python3
""" Running flask on 0.0.0.0, port 5000
which is also the default port
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0" port=5000)
