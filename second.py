import requests
from bs4 import BeautifulSoup

respond = requests.get("https://www.books.com.tw/web/sys_tdrntb/books")
soup = BeautifulSoup(respond.text, "html.parser")

bookMsgDivs = soup.find_all("div", class_="type02_bd-a")
for index,i in enumerate(bookMsgDivs):
    h4 = i.find("h4")
    #或是h4 = i.h4

    if h4:
        a = h4.find("a")
        #或是a = a.h4

        if a:
            print("排名: " + str(index+1) + " " + a.text)