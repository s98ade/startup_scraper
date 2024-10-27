import requests

from storage.storing import FileStorage
from parser.parser import Parser
from log import Logging
from utils.colors import bcolors


log_instance = Logging()
log = log_instance.get_logger()


class Scraper:
    def __init__(self, url: str):
        self.url = url
        self.storage = FileStorage()
        self.parser = Parser()
        
        
    def fetch_page(self, url):
        try:
            log.info(f"Fetching data from: {self.url}")
            response = requests.get(self.url)
            response.raise_for_status()
            log.info(f"Data retrieved successfully.")
            return response.text
        
        except requests.exceptions.HTTPError as http_err:
            log.error(f"HTTP error: {http_err}")
            print(f'{bcolors.FAIL}\nError fetching page: {http_err}\n')
            return None
        
        except Exception as err:
            log.error(f"Error: {err}")
            return None
        
    
    def scrape(self):
        content = self.fetch_page(self.url)
        
        if content:
            data = self.parser.parse_content(content)
            self.storage.save_in_csv(data) 
            self.storage.save_in_json(data)
            print(f'{bcolors.OKGREEN}\nData was scraped successfully.\nData stored in ../data/[filename].csv\n')
        else:
            print(f"{bcolors.FAIL}\nError: Content couldn't be retrieved.\n") # not sure whether the import of colors is correct