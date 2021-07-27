import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/search/?clid=9582&text=металлообработка%20в%20спб&l10n=en-US&lr=2'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
# print(soup)
# quotes = soup.find_all('div')
quotes = soup.find_all('a', {'class': 'Link Link_theme_outer Path-Item link path__item'})

for quote in quotes:
    print(quote)

# print(quotes)
