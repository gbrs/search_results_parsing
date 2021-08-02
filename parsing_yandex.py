import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/search/?text=металлообработка+спб&lr=2&p=9'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
# print(soup)
# quotes = soup.find_all('div')
quotes = soup.find_all('a', {'class': 'Link Link_theme_outer Path-Item link path__item'})

for quote in quotes:
    s = str(quote)
    s = s[s.find('href=') + 6::]
    s = s[:s.find('"'):]
    s = s.replace('http://', '').replace('https://', '').replace('www.', '')
    if 'yandex' not in s:
        print(s)

# print(quotes)
