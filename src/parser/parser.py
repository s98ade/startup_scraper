from bs4 import BeautifulSoup

class Parser:
    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        
        table = soup.find('tbody')
        
        for row in table.find_all('tr'):
            row_data = []
        
            for cell in row.find_all('td'):
                cell_text = cell.get_text(strip=True)
                row_data.append(cell_text)
                
        return row_data