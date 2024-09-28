import requests
from bs4 import BeautifulSoup # do I need this here?
import csv # do i need this here?

class Scraper:
    def __inti__(self, url: str):
        self.url = url
        self.storage = # class for the database and file handling
        self.parser = # class for specific parser
        
    def fetch_page(self, url):
        try:
            self.url = requests.get(url).text
            status = requests.status_codes
            return self.url
        except requests.exceptions.RequestException as error:
            return f'Error fetching page: {error}\nStatus {status}'
    
    def scrape(self):
        content = self.fetch_page()
        
        if content:
            data = # parser
            # function for storage

# -------------------------------------------------------------------------- #
soup = BeautifulSoup(url, 'html.parser') # this goes to parser

table = soup.find('tbody') # goes to parser

with open('../data/startup_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile) # this goes to storage
    
    for row in table.find_all('tr'): #this goes to parser
        row_data = []
        
        for cell in row.find_all('td'):
            cell_text = cell.get_text(strip=True) #strip off extra space from text
            row_data.append(cell_text)
            
        csvwriter.writerow(row_data) # goes to storage

print("Data retrieved...Information saved in ../data/startup_data.csv")