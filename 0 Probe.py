import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/search/?clid=9582&text=металлообработка%20в%20спб&l10n=en-US&lr=2'
# url = 'https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)'
# url = 'https://dev-gang.ru/article/rukovodstvo-po-sintaksiczeskomu-analizu-html-s-pomosczu-beautifulsoup-v-python-kgnmwzixct/'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')

print(soup)


# quotes = soup.find_all('div')
#
# for quote in quotes:
#     print(quote.text)
#