import requests
from bs4 import BeautifulSoup
import csv

url = requests.get('https://startup100.net/').text

soup = BeautifulSoup(url, 'html.parser')

table = soup.find('tbody')

with open('../data/startup_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for row in table.find_all('tr'):
        row_data = []
        
        for cell in row.find_all('td'):
            cell_text = cell.get_text(strip=True) #strip off extra space from text
            
            row_data.append(cell_text)
            
        csvwriter.writerow(row_data)

print("Data retrieved...Information saved in ../data/startup_data.csv")