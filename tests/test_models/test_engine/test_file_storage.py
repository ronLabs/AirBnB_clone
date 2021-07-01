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

    def tearDown(self):
        """ tearDown method that executes after each test method """

        del self.storage

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_all(self):
        """ testing all methods from FileStorage """

        """ testing all method from FileStorage """
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

        """ testing if is an instance of FileStorage class """
        self.assertIsInstance(self.storage, FileStorage)
        self.assertNotIsInstance(self.storage, BaseModel)

    def test_permissions(self):
        """ testing permissions of the file file_storage.py """

        file = 'models/engine/file_storage.py'
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))


if __name__ == '__main__':

    unittest.main()
