from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.models import Cars

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Cars(car_manufacturer="VW", car_colour="white", price="50000"))
        db.session.commit

    def tearDown(self):
        db.session.remove()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("index"))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):

    def test_Ford(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='Ford')
            test.get("http://service3-backend:5000/colour", text = 'red')
            test.post("http://service4-backend:5000/price", json = '30000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Ford', response.data)
            self.assertIn(b'red', response.data)
            self.assertIn(b'30000', response.data)
            

    def test_Lamborghini(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='Lamborghini')
            test.get("http://service3-backend:5000/colour", text = 'blue')
            test.post("http://service4-backend:5000/price", json = '25000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Lamborghini', response.data)
            self.assertIn(b'blue', response.data)
            self.assertIn(b'25000', response.data)
    
    def test_Mercedes(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='Mercedes')
            test.get("http://service3-backend:5000/colour", text = 'yellow')
            test.post("http://service4-backend:5000/price", json = '27000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'yellow', response.data)
            self.assertIn(b'27000', response.data)


    def test_BMW(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='BMW')
            test.get("http://service3-backend:5000/colour", text = 'black')
            test.post("http://service4-backend:5000/price", json = '35000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'black', response.data)
            self.assertIn(b'35000', response.data)

    def test_audi(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='Audi')
            test.get("http://service3-backend:5000/colour", text = 'white')
            test.post("http://service4-backend:5000/price", json = '40000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Audi', response.data)
            self.assertIn(b'white', response.data)
            self.assertIn(b'40000', response.data)

    def test_Ford1(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='Ford')
            test.get("http://service3-backend:5000/colour", text = 'blue')
            test.post("http://service4-backend:5000/price", json = '26000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Ford', response.data)
            self.assertIn(b'blue', response.data)
            self.assertIn(b'26000', response.data)

    def test_Lamborghini1(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='Lamborghini')
            test.get("http://service3-backend:5000/colour", text = 'yellow')
            test.post("http://service4-backend:5000/price", json = '23500')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Lamborghini', response.data)
            self.assertIn(b'yellow', response.data)
            self.assertIn(b'23500', response.data)
    
    def test_Mercedes1(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='Mercedes')
            test.get("http://service3-backend:5000/colour", text = 'red')
            test.post("http://service4-backend:5000/price", json = '28000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Mercedes', response.data)
            self.assertIn(b'red', response.data)
            self.assertIn(b'28000', response.data)


    def test_BMW1(self):
        with requests_mock.mock() as test:
            test.get("http://service2-backend:5000/car_name", text ='BMW')
            test.get("http://service3-backend:5000/colour", text = 'red')
            test.post("http://service4-backend:5000/price", json = '32000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'BMW', response.data)
            self.assertIn(b'red', response.data)
            self.assertIn(b'32000', response.data)

