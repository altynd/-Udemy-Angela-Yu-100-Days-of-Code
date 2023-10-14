import requests
from bs4 import BeautifulSoup

date = input("Which year songs yuo want YYYY-MM-DD:")
link = "https://www.billboard.com/charts/hot-100/"

endpoint = link+date+"/"

response = requests.get(endpoint).text
soup = BeautifulSoup(response, "lxml")

songs = []

containers = soup.find_all("div", class_="o-chart-results-list-row-container")
for container in containers:
    song = container.find("h3").text.strip()
    # print(song)
    artist = container.find("span", class_="a-no-trucate").text.strip()
    # print(artist)
    song={
        "song":song,
        "artist":artist
    }
    songs.append(song)

print(songs)

