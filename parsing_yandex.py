import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/search/?clid=9582&text=металлообработка%20в%20спб&l10n=en-US&lr=2'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div')

for quote in quotes:
    print(quote.text)

# print(quotes)
