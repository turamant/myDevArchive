#Импортируем библиотеки
import requests
from bs4 import BeautifulSoup

#Запрашиваем URL
page = requests.get("https://www.khl.ru/players/season/1154/")

#Скачиваем страницу
soup = BeautifulSoup(page.content, "html.parser")
#Скрапим данные
name = soup.find_all("p",
                     {"players-table__txt"})
for n in name:
    print(n.text.replace("\n","").strip())

