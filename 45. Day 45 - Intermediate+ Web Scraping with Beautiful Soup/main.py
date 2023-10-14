from bs4 import BeautifulSoup
import requests

link = "https://news.ycombinator.com/"

response = requests.get(link).text
soup = BeautifulSoup(response, "lxml")
# print(soup.prettify())
title_block = soup.find_all(class_="titleline")
points = soup.find_all(class_="subtext")

titles_list = [title.text for title in title_block]
href_list = [block.find("a").get("href") for block in title_block]
points_list = [item.find(class_="score") for item in points]
# print(points_list)

# for i in range(len(titles_list)):
#     print(titles_list[i])
#     print(href_list[i])
#     try:
#         print(points_list[i].text.split()[0])
#     except:
#         print("0")

# variant 1
max_point = 0
j = 0
for i in range(len(titles_list)):
    try:
        point = int(points_list[i].text.split()[0])
    except:
        point = 0
    if point>max_point:
        max_point = point
        j = i


print(titles_list[j])
print(href_list[j])
print(points_list[j].text.split()[0])