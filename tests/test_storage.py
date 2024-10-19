import unittest
from unittest.mock import mock_open, patch

from src.storage.storing import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()


    @patch("builtins.open", new_callable=mock_open)
    def test_save_in_csv(self, mock_file):
        data = {
            'Pibox': ['1. (141)', '667'],
            'Makea Games': ['2. (29)', '239']
        }
        self.file_storage.save_in_csv(data)

        mock_file.assert_called_once_with('../data/startup100.csv', mode='a', newline='', encoding='utf-8')
        
        mock_file().write.assert_called()  # Ensure that writing happened


    @patch("builtins.open", new_callable=mock_open)
    def test_save_in_csv_empty_data(self, mock_file):
        data = {}
        self.file_storage.save_in_csv(data)

        mock_file.assert_called_once()