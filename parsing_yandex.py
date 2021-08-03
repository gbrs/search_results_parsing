'''
Спарсить адреса конкурентов из поисковой выдачи Яндекса.
'''

'''
Обход защиты Яндекса от роботов нужен.
Дописать для определения позициии нашего сайта в поисковой выдаче?
'''


import requests
from bs4 import BeautifulSoup

# из человеческого поискового запроса леплю яндексовский
human_search_query = 'изготовление шестерен в спб'
human_search_query = human_search_query.split()
spam = human_search_query[0]
for word in human_search_query[1:]:
    spam = '+'.join((spam, word))
url = 'https://yandex.ru/search/?text=' + spam + '&lr=2' + '&clid=9582&src=suggest_B'  # + '&numdoc=50' + '&p=2'

# запрос - ответ - суп - отбор ссылок на сайты
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)
# quotes = soup.find_all('div')
quotes = soup.find_all('a', {'class': 'Link Link_theme_outer Path-Item link path__item'})

# достаем hrefы из ссылок, удаляем "ненужные слова"
# и все ссылки, предлагаемые Яндексом (директ, карты...)
for quote in quotes:
    s = str(quote)
    s = s[s.find('href=') + 6::]
    s = s[:s.find('"'):]
    s = s.replace('http://', '').replace('https://', '').replace('www.', '')
    if 'yandex' not in s:
        print(s)

# print(quotes)
