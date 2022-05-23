# Scrapes YC News for the article with the highest votes today

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
page = response.text

soup = BeautifulSoup(page, "html.parser")

article_titles = soup.find_all(name="a", class_="titlelink")
article_score = soup.find_all(name="span", class_="score")
titles = []
links = []
score = []

for items in article_titles:
    titles.append(items.getText())
    links.append(items.get("href"))

for items in article_score:
    text = items.getText()
    number = int(text.split()[0])
    score.append(number)

highest_vote = max(score)
index = score.index(highest_vote)
print(f"{titles[index]}\n {links[0]}\n Votes: {highest_vote}")