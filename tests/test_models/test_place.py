#!/usr/bin/python3
"""Unittest Place"""

import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class testPlace(unittest.TestCase):
    """test cases for the Place class"""

    def test_init(self):
        """test instantiation of Place class"""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attributes(self):
        """test the attributes of Place class"""
        p = Place()
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "created_at"))
        self.assertTrue(hasattr(p, "updated_at"))
        self.assertTrue(hasattr(p, "id"))
        self.assertTrue(hasattr(p, "user_id"))
        self.assertTrue(hasattr(p, "city_id"))

    def test_to_dict(self):
        """test to_dict"""
        p = Place()
        self.assertEqual("to_dict" in dir(p), True)

    def test_functions(self):
        """test functions"""
        self.assertIsNotNone(Place.__doc__)

    def test_save(self):
        """test save"""
        p = Place()
        p.save()
        self.assertNotEqual(p.created_at, p.updated_at)

    def test_strings(self):
        """test strings"""
        p = Place()
        self.assertEqual(type(p.name), str)
        self.assertEqual(type(p.id), str)

if __name__ == "__main__":
    unittest.main()
