#!/usr/bin/python3


"""
Flask Web App

Flask web app defines three routes: '/', '/hbnb', and '/c/<text>'. The '/' route returns the string "Hello HBNB!", the '/hbnb' route returns the string "HBNB", and the '/c/<text>' route returns the string "C " followed by the value of the 'text' variable with underscores replaced by spaces.

"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
