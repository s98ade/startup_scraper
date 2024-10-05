from bs4 import BeautifulSoup

# Parser completely broken! Also look into csv-storing
class Parser:
    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        
        table = soup.find('tbody')
        
        result = []
        
        for row in table.find_all('tr'):
            row_data = []
        
            for cell in row.find_all('td'):
                cell_text = cell.get_text(strip=True)
                row_data.append(cell_text)
            
            result.append(row_data)
            
        return result