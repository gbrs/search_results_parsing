import requests
from bs4 import BeautifulSoup

def parse_site(site_name):

    url = 'https://ferropolis.ru/'
    response = requests.get(url)

    #  исправляем кодировку на некоторых сайтах
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('p') + soup.find_all('ul') + soup.find_all('ol')
    # абзацы, списки (маркированные и нумерованные)

    with open('output.txt', 'a', encoding='utf-8') as f:
        for quote in quotes:
            txt = quote.text
            f.write(txt)
            f.write('\n')
            # quote.txt здесь возвращал None, а внутри print - строку.
            # пришлось ввести промежуточную переменную txt

