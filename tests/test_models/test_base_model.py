#!/usr/bin/python3
""" Unittests for BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for BaseModel"""

    def setUp(self):
        """setup method"""

        self.a = BaseModel()
        self.b = BaseModel()
