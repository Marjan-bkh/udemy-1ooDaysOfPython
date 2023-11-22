import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(url=URL).text
soup=BeautifulSoup(response,"html.parser")
soup_title=soup.findAll("h3",class_="title")
title_list= [title.getText() for title in soup_title ]
with open ("movies.txt","w",encoding="utf-8") as file:
    [ file.write(item+"\n") for item in reversed(title_list)]



# Write your code below this line 👇


chrome_driver_path="D:\GitHub\Sazman\Codes\Bakhtiari\udemy\chromedriver.exe"