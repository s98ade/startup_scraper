import unittest
import requests_mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))) #should solve path issue

from src.scraper.su100_scraper import Scraper


class TestScraper(unittest.TestCase):
    def setUp(self):
        self.url = "https://example.com"
        self.scraper = Scraper(self.url)
        
    
    @requests_mock.Mocker()
    def test_fetch_content_success(self, mocker):
        mocker.get(self.url, test="html><body><h1>Test</h1></body></html>")
        
        content = self.scraper.fetch_page()
        
        self.assertIn("<html>", content.decode('utf-8'))
        
    
    @requests_mock.Mocker()
    def test_fetch_content_failure(self, mocker):
        mocker.get(self.url, status_code=404)
        
        content = self.scraper.fetch_page(self.url)
        
        self.assertIsNone(content)