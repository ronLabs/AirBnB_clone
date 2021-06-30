#!/usr/bin/python3
""" Unittests for BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for BaseModel"""

    def setUp(self):
        """setup method"""

        self.base1 = BaseModel()
        self.base1.name = "Lorem ipsum"
        self.base1.number = 777
    
    def test_id(self):
        """ testing instance id """

        new_instance = BaseModel()
        new_instance_2 = BaseModel()

        """ testing if the id's are not equals """
        self.assertNotEqual(self.base1.id, new_instance.id)
        self.assertNotEqual(new_instance.id, new_instance_2.id)
        self.assertNotEqual(self.base1.id, new_instance_2.id)

        """ testing if the id's are of type str """
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(new_instance.id, str)
        self.assertIsInstance(new_instance_2.id, str)

    def test_save(self):
        """ testing save method from BaseModel """

        new_instance = BaseModel()

        self.base1.save()
        new_instance.save()

        """ testing if the update_at attribute is from datetime type """
        self.assertIsInstance(self.base1.updated_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

    def test_to_dict(self):
        """ testing to_dict method from BaseModel class """

        to_dict = self.base1.to_dict()

        """ testing if the return value of to dict method is dict """
        self.assertIsInstance(to_dict, dict)

        """ testing the keys of the to_dict dictionary """
        self.assertIsInstance(to_dict['id'], str)
        self.assertIsInstance(to_dict['created_at'], str)
        self.assertIsInstance(to_dict['updated_at'], str)
        self.assertIsInstance(to_dict['name'], str)
        self.assertIsInstance(to_dict['number'], int)

        self.assertEqual(to_dict['name'], "Lorem ipsum")
        self.assertEqual(to_dict['number'], 777)

if __name__ == "__main__":
    """ if it's executed as main program """
    unittest.main()
