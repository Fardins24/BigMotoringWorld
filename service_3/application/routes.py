from application import app
from flask import request, Response
import random

@app.route("/colour", methods=["GET"])
def get_colour():
    colours = ["red", "blue",  "yellow", "black", "white", "green"]
    return Response(random.choice(colours))