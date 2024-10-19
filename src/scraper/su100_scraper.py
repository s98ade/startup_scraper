import requests

from storage import storing
from parser import parser
from log import Logging
from utils import colors


log_instance = Logging()
log = log_instance.get_logger()


class Scraper:
    def __init__(self, url: str):
        self.url = url
        self.storage = storing.FileStorage()
        self.parser = parser.Parser()
        
        
    def fetch_page(self, url):
        try:
            log.info(f"Fetching data from: {self.url}")
            self.url = requests.get(url).text
            status = requests.status_codes
            log.info(f"Data retrieved successfully.")
            return self.url
        except requests.exceptions.HTTPError as http_err:
            log.error(f"HTTP error: {http_err}")
            print(f'{colors.bcolors.FAIL}\nError fetching page: {http_err}\nStatus {status}\n')
            return None
        except Exception as err:
            log.error(f"Error: {err}")
        
    
    def scrape(self):
        content = self.fetch_page(self.url)
        
        if content:
            data = self.parser.parse_content(content)
            self.storage.save_in_csv(data) 
            print(f'{colors.bcolors.OKGREEN}\nData was scraped successfully.\nData stored in ../data/[filename].csv\n')
        else:
            print(f"{colors.bcolors.FAIL}\nError: Content couldn't be retrieved.\n") # not sure whether the import of colors is correct