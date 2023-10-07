import  requests
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/d036caae7310566a4a07393568081a50/flightDeals/prices"

    def load_data(self):
        """ get information from googlesheet"""

        response = requests.get(url=self.sheety_endpoint)
        response.raise_for_status()
        data = response.json()["prices"]
        for string in data:
            string["code"] = FlightSearch().code(string["city"])

            string["codefrom"] = FlightSearch().code(string["cityfrom"])
        return data


    def put_data(self, data_info):#works
        """post information to googlesheet"""
        headers ={
            "Content-Type":"application/json"
        }

        data = {
            "price":{
                "cityfrom": data_info["city_from"],
                "pricemin": data_info["price_min"],
                "cityto": data_info["city_to"],
                "datetime": data_info["datetime"],
            }
        }


        response = requests.put(url=f"{self.sheety_endpoint}/2", json=data, headers=headers)
        response.raise_for_status()
