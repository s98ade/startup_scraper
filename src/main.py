import requests
from bs4 import BeautifulSoup
import csv

url = requests.get('https://startup100.net/').text

soup = BeautifulSoup(url, 'html.parser')

table = soup.find('table')

tbody = table.tbody

print(tbody.prettify())
# print(table.prettify())
# print(soup.prettify())
