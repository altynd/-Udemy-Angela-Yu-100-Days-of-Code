import requests

USERNAME = "altynd2"
TOKEN = "dfbsdfhsdfhdfbdfbsdfb"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

parameters_graph = {
    "id": GRAPH_ID,
    "name": "my_study_graph",
    "unit": "h",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
##create graph
# response = requests.post(url=graph_endpoint, json=parameters_graph, headers=headers)
# print(response.text)

one_day_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

from datetime import datetime

today = datetime.today().strftime("%Y%m%d")
parameters_pixel = {
    "date": today,
    "quantity": "6",
}
# # add pixel
# response = requests.post(url=one_day_endpoint, json=parameters_pixel,
#                          headers=headers)
# print(response.text)

#change pixel
change_endpoint = f"{one_day_endpoint}/{today}"
parameters_change = {
    "quantity":"15"
}
response = requests.put(url=change_endpoint,json=parameters_change, headers=headers)
print(response.text)