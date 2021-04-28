import requests
from bs4 import BeautifulSoup

url = 'http://kvadromash.ru'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')  # имеет собственный тип данных
quotes = soup.find_all('p')  # имеет собственный тип данных

for quote in quotes:  # quote имеет собственный тип данных
    print(quote.text)  # выдает тип "строка"
