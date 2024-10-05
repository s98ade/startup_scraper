import requests

from storage import storing
from parser import parser
from utils import colors


class Scraper:
    def __init__(self, url: str):
        self.url = url
        self.storage = storing.FileStorage()
        self.parser = parser.Parser()
        
        
    def fetch_page(self, url):
        try:
            self.url = requests.get(url).text
            status = requests.status_codes
            return self.url
        except requests.exceptions.RequestException as error:
            print(f'{colors.bcolors.FAIL}\nError fetching page: {error}\nStatus {status}\n')
            return None
        
    
    def scrape(self):
        content = self.fetch_page(self.url)
        
        if content:
            data = self.parser.parse_content(content)
            """ for row in data: # TEST
                print(row) # TEST """
            self.storage.save_in_csv(data) 
            print(f'{colors.bcolors.OKGREEN}\nData was scraped successfully.\nData stored in ../data/[filename].csv\n')
        else:
            print(f"{colors.bcolors.FAIL}\nError: Content couldn't be retrieved.\n") # not sure whether the import of colors is correct