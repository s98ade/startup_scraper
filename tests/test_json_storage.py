import unittest
from unittest.mock import mock_open, patch
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.storage.storing import FileStorage


class TestJsonStorage(unittest.TestCase):
    def setUp(self):
        self.json_storage = FileStorage()
        
    
    @patch("builtins.open", new_callable=mock_open)
    def test_save_in_json(self, mock_file):
        data = {
            'Pibox': ['1. (141)', '667'],
            'Makea Games': ['2. (29)', '239']
        }
        self.json_storage.save_in_json(data)
        
        mock_file.assert_called_once_with('../data/startup100.json', mode='a', newline='', encoding='utf-8')
        
        mock_file().write.assert_called()
        
    
    @patch("builtins.open", new_callable=mock_open)
    def test_save_in_json_empty_data(self, mock_file):
        data = {}
        self.json_storage.save_in_json(data)

        mock_file.assert_called_once()