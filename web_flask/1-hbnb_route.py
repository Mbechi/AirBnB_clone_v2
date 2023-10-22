#!/usr/bin/python3


"""
Flask web app defines two routes: '/' and '/hbnb'. 

When a user accesses the root URL ('/'), the index() function is called and it returns the string 'Hello HBNB!'. 

When a user accesses the '/hbnb' URL, the hbnb() function is called and it returns the string 'HBNB'. 

The Flask application is then run on the host '0.0.0.0' and port '5000'.
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
