#!/usr/bin/python3
"""Unittest City class"""

import unittest
import os
from models.city import City
from models.base_model import BaseModel


class testCity(unittest.TestCase):
    """test the City class"""

    def test_init(self):
        """test instantiation of City class"""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_attributes(self):
        """test the attributes of City class"""
        new_city = City()
        self.assertTrue(hasattr(new_city, "name"))
        self.assertTrue(hasattr(new_city, "created_at"))
        self.assertTrue(hasattr(new_city, "updated_at"))
        self.assertTrue(hasattr(new_city, "id"))
        self.assertTrue(hasattr(new_city, "state_id"))

    def test_to_dict(self):
        """test to_dict"""
        city = City()
        self.assertEqual("to_dict" in dir(city), True)

    def test_functions(self):
        """test functions"""
        self.assertIsNotNone(City.__doc__)

    def test_save(self):
        """test save"""
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_strings(self):
        """test strings"""
        city = City()
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.state_id), str)

if __name__ == "__main__":
    unittest.main()
