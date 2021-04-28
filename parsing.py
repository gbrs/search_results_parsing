import requests
from bs4 import BeautifulSoup

url = 'http://kvadromash.ru'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('p')

for quote in quotes:
    print(quote.text)

# print(quotes)
