from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase


from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_get_car_name(self):
        for i in range(5):
            response = self.client.get(url_for('get_car'))
            car_list = [b"Ford", b"Lamborghini", b"Mercedes", b"BMW", b"Audi"]
            self.assertIn(response.data, car_list)

            