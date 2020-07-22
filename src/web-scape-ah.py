import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.authentic-happiness.com/')
html = BeautifulSoup(req.content, 'html.parser')
print(html.find_all('a'))