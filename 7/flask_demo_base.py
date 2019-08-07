#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://flask.pocoo.org/

sample flask demo

app.run()
http://127.0.0.1:5000/

app.run("", 8000)
http://localhost:8000/
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# host=None, port=None, debug=None, **options
app.run()
