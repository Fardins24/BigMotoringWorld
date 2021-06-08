from application import app
from flask import request, Response
import random

@app.route("/car_name", methods=["GET"])
def get_car():
    cars = ["Ford", "Nissan", "Toyota", "BMW", "Audi"]
    return Response(str(random.choice(cars)))