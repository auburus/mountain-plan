# pylint: disable=missing-function-docstring

from flask import render_template

from app import app


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html.j2")
