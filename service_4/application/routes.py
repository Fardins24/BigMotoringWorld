from application import app
from flask import request, Response
import random

@app.route("/price", methods=["GET", "POST"])
def price():
    package=request.get_json()
    
    if package['car_make'] == 'Ford' and package['car_colour'] == 'red':
        car_price = 30000
    elif package['car_make'] == 'Mercedes' and package['car_colour'] == 'blue':
        car_price = 25000
    elif package['car_make'] == 'Lamborghini' and package['car_colour'] == 'yellow':
        car_price = 100000
    elif package['car_make'] == 'BMW' and package['car_colour'] == 'black':
        car_price = 35000
    elif package['car_make'] == 'Audi' and package['car_colour'] == 'black':
        car_price = 40000  
    elif package['car_make'] == 'Ford' and package['car_colour'] == 'blue':
        car_price = 26000
    elif package['car_make'] == 'Mercedes' and package['car_colour'] == 'yellow':
        car_price = 23500
    elif package['car_make'] == 'Lamborghini' and package['car_colour'] == 'red':
        car_price = 280000
    elif package['car_make'] == 'BMW' and package['car_colour'] == 'red':
        car_price = 32000
    elif package['car_make'] == 'Toyota' and package['car_colour'] == 'green':
        car_price = 78000
    elif package['car_make'] == 'Nissan' and package['car_colour'] == 'white':
        car_price = 62000
    else:
        car_price = 12000  

    return Response(str(car_price))
