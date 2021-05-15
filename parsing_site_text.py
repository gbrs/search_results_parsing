import requests
from bs4 import BeautifulSoup

def parse_site(url):
    '''
    парсит текст с сайта по указанному адресу
    :param url: адрес сайта, который парсим
    :return: None. (До)записывает в файл текст сайта
    '''

    response = requests.get(url)

    #  исправляем кодировку на некоторых сайтах
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('p') + soup.find_all('ul') + soup.find_all('ol')
    # абзацы, списки (маркированные и нумерованные)

    with open('output.txt', 'a', encoding='utf-8') as f:
        for quote in quotes:
            txt = quote.text
            if txt != '\n':  # TODO не работает условие - куча пустых строк. Почему?
                f.write(txt)
                f.write('\n')
            # quote.txt здесь возвращал None, а внутри print - строку.
            # пришлось ввести промежуточную переменную txt
        f.write(3 * '_____________________________________________________________________________\n')


with open('urls.txt', encoding='utf-8') as f:
    urls = f.read().split()
print(urls)

for url in urls:
    parse_site(url)
