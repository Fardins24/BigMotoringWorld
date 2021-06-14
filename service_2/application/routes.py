from application import app
from flask import request, Response
import random

@app.route("/car_name", methods=["GET"])
def get_car():
    cars = ["Ford", "Lamborghini", "Mercedes", "BMW", "Audi", "Toyota", "Nissan"]
    return Response(random.choice(cars))