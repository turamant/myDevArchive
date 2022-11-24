#Импортируем библиотеки
import requests
from bs4 import BeautifulSoup

#Запрашиваем URL
page = requests.get("https://www.khl.ru/players/17968/")

id_list = list()
#Скачиваем страницу
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
#Скрапим данные
all = soup.find_all("div", "frameCard-header__detail-item")
for i in all:
    print(i.text.replace("\n", "").strip())

all = soup.find_all("div", "hover-table__part hover-table__part--left")
for i in all:
    print(i.text.replace("\n", "").strip())