import requests
from bs4 import BeautifulSoup

url = 'https://ferropolis.ru/'
response = requests.get(url)
response.encoding = 'utf-8'
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('p') + soup.find_all('ul') + soup.find_all('ol')
# абзацы, списки (маркированные и нумерованные)

with open('output.txt', 'w', encoding='utf-8') as f:
    for quote in quotes:
        # print(quote.text)
        f.write(quote.txt)  # TODO quote.txt возвращает None

# print(quotes)
