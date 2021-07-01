#!/usr/bin/python3
""" Unit testing for FileStorage class """

import os
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Class to making unittesting for FileStorage class """

    def setUp(self):
        """ setUp method that executes before each test method """

        self.storage = FileStorage()

    def test_all(self):
        """ testing all methods from FileStorage """

        """ testing all method from FileStorage """
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

        """ testing if is an instance of FileStorage class """
        self.assertIsInstance(self.storage, FileStorage)
        self.assertNotIsInstance(self.storage, BaseModel)

if __name__ == '__main__':

    unittest.main()
