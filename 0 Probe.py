import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data_items(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('a', {'class' : 'link link_outer_yes link_theme_outer path__item i-bem'})

    return [a.get('href') for a in items]


def main():
    url = 'https://yandex.ru/search/?clid=9582&text=скачать&lr=118890&p=1'
    print(get_data_items(get_html(url)))


if __name__ == '__main__':
    main()
