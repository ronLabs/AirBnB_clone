#!/usr/bin/python3
""" Unittests for BaseModel"""

import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
import time


class TestBaseModel(unittest.TestCase):
    """Test case for BaseModel"""

    def setUp(self):
        """setup method"""

        self.base1 = BaseModel()
        self.base2 = BaseModel()
        self.base1.name = "Lorem ipsum"
        self.base1.number = 777

    def test_pep8(self):
        """test pep8 format"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_base_model(self):
        """test that the instatiation of a BaseModel"""
        new_instance = BaseModel()
        new_instance_2 = BaseModel()

        self.assertEqual(type(new_instance), BaseModel)

        """test created_at, updated_at is a instance of type datetime"""
        self.assertTrue(new_instance.created_at is not None)
        self.assertEqual(type(new_instance.created_at), datetime)
        self.assertTrue(new_instance.updated_at is not None)
        self.assertEqual(type(new_instance.updated_at), datetime)

        """test two BaseModel instances have different datetime objects"""
        self.assertNotEqual(new_instance.created_at, new_instance_2.created_at)
        self.assertNotEqual(new_instance.updated_at, new_instance_2.updated_at)

        """test updated_at and created_at are the same for a new instance"""
        self.assertEqual(new_instance.updated_at, new_instance.created_at)

    def test_dict_contents(self):
        """test contents inside dictionary"""
        self.assertTrue(getattr(self.base1, '__class__'))
        self.assertTrue(getattr(self.base1, 'created_at'))
        self.assertTrue(getattr(self.base1, 'updated_at'))
        self.assertTrue(getattr(self.base1, 'id'))
        with self.assertRaises(AttributeError):
            getattr(self.base2, 'Hello')
        self.assertTrue(getattr(self.base1, 'name'))

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
        old_newInstance = new_instance.updated_at
        time.sleep(2)
        new_instance.save()

        """ testing if the update_at attribute is from datetime type """
        self.assertIsInstance(self.base1.updated_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)
        self.assertNotEqual(new_instance, old_newInstance)

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
        self.assertEqual(to_dict['__class__'], 'BaseModel')

    def test_str(self):
        """test the str method has the correct output"""
        bm = BaseModel()
        string = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(string, str(bm))

    def test_kwargs(self):
        """ test kwargs init """
        bm = BaseModel()
        bm1 = BaseModel(**bm.to_dict())
        self.assertEqual(bm.to_dict(), bm1.to_dict())
        self.assertNotEqual(bm, bm1)

if __name__ == "__main__":
    """ if it's executed as main program """
    unittest.main()
