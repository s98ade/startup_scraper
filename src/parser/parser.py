import re
from bs4 import BeautifulSoup

from utils.colors import bcolors
from log import Logging


log_instance = Logging()
log = log_instance.get_logger()


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
                    company_data = {
                        "Company": company_name,
                        "S100 Index": cells[2].get_text(strip=True),
                        "Category": cells[3].get_text(strip=True),
                        "Founding Year": cells[4].get_text(strip=True),
                        "Location": cells[5].get_text(strip=True),
                        "Funding": cells[6].get_text(strip=True),
                        "Revenue": re.sub(r'\s+', ' ', cells[7].get_text(strip=True)).replace('\n', ' ').strip(),
                        "Business ID": cells[8].get_text(strip=True)
                    }
                    result[company_name] = company_data             
        except AttributeError as e:
            log.error(f"Table not found: {e}")
            print(f"{bcolors.FAIL}Error: Table not found!\n")

        return result