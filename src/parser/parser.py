from bs4 import BeautifulSoup


class Parser:
    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        
        table = soup.find('tbody')
        
        result = {}
        
        for row in table.find_all('tr'):
            cells = row.find_all('td')

            if len(cells) > 1:
                company_name = cells[1].get_text(strip=True)
                row_data = [cell.get_text(strip=True) for index, cell in enumerate(cells) if index != 1]
                result[company_name] = row_data

        return result