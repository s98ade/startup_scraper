from bs4 import BeautifulSoup

from src.utils.colors import bcolors
from src.log import Logging


log_instance = Logging()
log = log_instance.get_logger()

# needs error handling in edge cases like does not found 'tbody' or other components
class Parser:
    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        
        try:
            table = soup.find('tbody')
            
            result = {}
            
            for row in table.find_all('tr'):
                cells = row.find_all('td')

                if len(cells) > 1:
                    company_name = cells[1].get_text(strip=True)
                    row_data = [cell.get_text(strip=True) for index, cell in enumerate(cells) if index != 1]
                    result[company_name] = row_data
                    
        except AttributeError as e:
            log.error(f"Table not found: {e}")
            print(f"{bcolors.FAIL}Error: Table not found!\n")

        return result