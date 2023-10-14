import requests
from bs4 import BeautifulSoup


link = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(link).text
soup = BeautifulSoup(response, "lxml")

blocks = soup.find_all(class_="listicle_listicle__item__OCDTx")
blocks.reverse()
number = 1
output = ""
for block in blocks:
    title = block.find("h3").text
    output+=f"{title}\n"

with open("movies.txt", "w") as file:
    file.write(output)


