#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("web_home.html")


@app.route("/sign_in", methods=["GET"])
def sign_in_form():
    return render_template("web_login.html")


@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "123456":
        return render_template("web_ok.html", username=username)
    return render_template("web_login.html", message="Bad username or password", username=username)


if __name__ == '__main__':
    app.run()
