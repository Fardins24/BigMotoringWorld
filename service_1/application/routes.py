from application import app, db
from application.models import Cars
from flask import render_template
from sqlalchemy import desc
import requests

@app.route('/')
def index():  
    car_make = requests.get("http://service2-backend:5000/car_name")
    car_colour = requests.get("http://service3-backend:5000/colour")
    price = requests.post("http://service4-backend:5000/price", json={'car_make':car_make.text, 'car_colour':car_colour.text})
    
    car = Cars(car_manufacturer = car_make.text, car_colour = car_colour.text, price=price.text)
    
    db.session.add(car)
    db.session.commit()
    cars = Cars.query.order_by(Cars.id.desc()).limit(5)
    
    return render_template("index.html", car_name=car_make.text, colour=car_colour.text, cars=cars, price=price.text)


