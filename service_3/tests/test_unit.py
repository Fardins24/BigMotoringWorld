from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase


from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_get_car_colour_red(self):
        with patch("random.choice") as random:
            random.return_value = "red" 
            response = self.client.get(url_for('get_colour'))
            self.assertEqual(b'red', response.data)

    def test_get_car_colour_blue(self):
        with patch("random.choice") as random:
            random.return_value = "blue" 
            response = self.client.get(url_for('get_colour'))
            self.assertEqual(b'blue', response.data)

    def test_get_car_colour_yellow(self):
        with patch("random.choice") as random:
            random.return_value = "yellow" 
            response = self.client.get(url_for('get_colour'))
            self.assertEqual(b'yellow', response.data)

    def test_get_car_colour_black(self):
        with patch("random.choice") as random:
            random.return_value = "black" 
            response = self.client.get(url_for('get_colour'))
            self.assertEqual(b'black', response.data)

    
