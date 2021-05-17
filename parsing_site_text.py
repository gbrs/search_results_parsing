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
            # print(quote.text)
            txt = quote.text
            f.write(txt)
            f.write('\n')
            # quote.txt здесь возвращал None, а внутри print - строку.
            # пришлось ввести промежуточную переменную txt
        f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' * 3)


def erase_line_break(file_name):
    '''
    стирает пустые строки из файла
    :param file_name: обрабатываемый файл
    :return: перезаписывает обработанный файл
    '''
    with open('output.txt', encoding='utf-8') as f:
        txt = f.read()
        while '\n\n' in txt:
            txt = txt.replace('\n\n', '\n')
        # print(txt)

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(txt)


with open('urls.txt', encoding='utf-8') as f:
    urls = f.read().split()
print(urls)

for url in urls:
    parse_site(url)

erase_line_break('output.txt')
