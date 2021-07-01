#!/usr/bin/python3
""" Unit testing amenity class """

import os
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class Testamenity(unittest.TestCase):
    """ Class to make unit testing for amenity class """

    def setUp(self):
        """ setUp method that executes before each test method """

        self.amenity1 = Amenity()
        self.amenity1.name = "No se que podria ir aqui pero coloco esto :3"

    def tearDown(self):
        """ tearDown method that executes after each test method """

        del self.amenity1

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attributes(self):
        """ testing the attributes of amenity Class """

        attr = self.amenity1.to_dict()

        """ testing if the attributes exists in the instance """
        self.assertTrue('name' in attr)
        self.assertTrue('created_at' in attr)
        self.assertTrue('updated_at' in attr)
        self.assertTrue('id' in attr)
        self.assertTrue('__class__' in attr)

        """ testing the types of the attributes """
        self.assertIsInstance(self.amenity1.name, str)
        self.assertIsInstance(self.amenity1.id, str)
        self.assertIsInstance(self.amenity1.created_at, datetime)
        self.assertIsInstance(self.amenity1.updated_at, datetime)

    def test_inheritance(self):
        """ Testing if amenity class inherits from BaseModel class """

        self.assertIsInstance(self.amenity1, BaseModel)

    def test_permissions(self):
        """ testing permissions of the file amenity.py """

        file = 'models/amenity.py'
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))


if __name__ == "__main__":
    """ if it's executed as main program """

    unittest.main()
