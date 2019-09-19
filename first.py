import requests
from bs4 import BeautifulSoup

respond = requests.get("https://www.books.com.tw/web/sys_tdrntb/books")
soup = BeautifulSoup(respond.text, "html.parser")

bookMsgDivs = soup.find_all("div", class_="type02_bd-a")
for i in bookMsgDivs:
    h4 = i.find("h4")
    a = h4.find("a")
    if a:
        print(a.text)