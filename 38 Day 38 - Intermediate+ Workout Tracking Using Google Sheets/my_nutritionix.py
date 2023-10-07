# import requests
#
# NUTRI_APP_ID = "764891d1"
# NUTRI_APP_KEY = "a35a1609db02cfc17e00810a027dcc11"
#
# endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
#
# my_text = "for breakfast i ate 2 eggs"
#
# headers = {
#     "Content-Type":"application/json",
#     "x-app-id":NUTRI_APP_ID,
#     "x-app-key":NUTRI_APP_KEY,
# }
#
# data={
#     "query": my_text,
# }
#
# response = requests.post(url=endpoint, headers=headers, json=data)
# print(response.text)

import datetime
import requests

NUTRI_APP_ID = "764891d1"
NUTRI_APP_KEY = "a35a1609db02cfc17e00810a027dcc11"
GENDER = "male"
WEIGHT = 90
HEIGHT = 180
AGE = 38


def get_data(my_text):  #works
    """geet info from my text for googleshet"""

    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    headers = {
        "Content-Type": "application/json",
        "x-app-id": NUTRI_APP_ID,
        "x-app-key": NUTRI_APP_KEY,
    }
    body = {
        "query": my_text,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE
    }

    response = requests.post(url=endpoint, headers=headers, json=body)
    response.raise_for_status()

    # OUTPUT
    data = response.json()
    # print(data)
    # {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 30.02, 'met': 9.8, 'nf_calories': 441.29, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}]}
    date = datetime.datetime.now().date().strftime("%d/%m/%Y")
    time = datetime.datetime.now().time().strftime("%H:%M:%S")
    exercise = data["exercises"][0]["user_input"]
    duration = data["exercises"][0]["duration_min"]
    calories = data["exercises"][0]["nf_calories"]
    data_info = {
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }

    return data_info

if __name__ == "__main__":
    get_data("teaching Python 1 hour")