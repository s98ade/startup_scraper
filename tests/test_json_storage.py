import unittest
from unittest.mock import mock_open, patch
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.storage.storing import FileStorage


class TestJsonStorage(unittest.TestCase):
    def setUp(self):
        self.json_storage = FileStorage()
        
    
    