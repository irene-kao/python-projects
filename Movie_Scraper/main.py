# Pulls the 100 best movies of all time from empireonline.com

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies = []
titles = soup.find_all(name="h3", class_="title")
for item in titles:
    text = item.getText()
    movies.append(text)


movies_list = movies[::-1]

with open("movies.txt", mode="w") as file:
    for item in movies_list:
        file.write(f"{item}\n")
