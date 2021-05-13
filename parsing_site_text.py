import requests
from bs4 import BeautifulSoup

url = 'https://steelroof.ru/gibka/'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('p')

for quote in quotes:
    print(quote.text)
    # print(quote.text.encode('utf-8', 'replace').decode('utf-8', 'replace'))

# print(quotes)
