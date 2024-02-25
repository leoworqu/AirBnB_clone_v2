#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.

Routes:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: Displays "C " followed by the value of the text variable 
               (replace underscore _ symbols with a space)

The option strict_slashes=False is used in route definitions.
"""


from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display 'Hello HBNB!'."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route to display 'C ' followed by the value of the text variable."""
    return 'C {}'.format(escape(text).replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
