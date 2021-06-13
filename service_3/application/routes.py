from application import app
from flask import request, Response
import random

@app.route("/colour", methods=["GET"])
def get_colour():
    colours = ["red", "blue",  "yellow", "black"]
    return Response(random.choice(colours))