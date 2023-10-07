import requests
import datetime


def load_data():#works
    """ get information from googlesheet"""

    endpoint = "https://api.sheety.co/d036caae7310566a4a07393568081a50/myWorkouts/workouts"

    response = requests.get(url=endpoint)
    response.raise_for_status()

    return response.text


def post_data(data_info):#works
    """post information to googlesheet"""

    endpoint = "https://api.sheety.co/d036caae7310566a4a07393568081a50/myWorkouts/workouts"

    headers ={
        "Content-Type":"application/json"
    }

    data = {
        "workout":{
            "date": data_info["date"],
            "time": data_info["time"],
            "exercise": data_info["exercise"],
            "duration": data_info["duration"],
            "calories": data_info["calories"],
        }
    }


    response = requests.post(url=endpoint, json=data, headers=headers)
    response.raise_for_status()
