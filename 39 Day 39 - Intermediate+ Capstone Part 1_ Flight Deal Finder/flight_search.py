import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api = "BcPdChP-ywaIi-dikFNjE4TDRkyJt5Sb"


    def search(self, data_from_sheet):

        # data = {'city': 'Paris', 'code': 'PAR', 'price': 250}
        data = data_from_sheet

        # TODO make date from google sheet today and today +7 days
        date_from = "04/10/2023"  # tomorrow
        date_to = "14/10/2023"  # tomorrow +7days

        headers = {
            "Content-Type": "application/json",
            "Content-Encoding": "gzip",
            "apikey": self.api,
        }

        endpoint = "https://api.tequila.kiwi.com/v2/search"

        parameters = {
            "fly_from": data["codefrom"],
            "fly_to": data["code"],
            "date_from": date_from,
            "date_to": date_to,
            "price_to": data["price"]
        }

        response = requests.get(url=endpoint, headers=headers,
                                params=parameters)
        response.raise_for_status()
        flight_data_data = response.json()
        # print(flight_data_data)


        flight_data_min = None

        for flights_data in flight_data_data["data"]:
            price_max = 1000

            # print(flights_data["price"])
            if flights_data["price"] < price_max:
                flight_data_min = flights_data

        return flight_data_min

    def code(self,city):

        endpoint = f"https://api.tequila.kiwi.com/locations/query?term={city.lower()}&locale=en-US&location_types=airport&limit=10&active_only=true' \
"
        # parameters = {
        #     "term": city.lower()
        # }

        headers = {
            "accept": "application/json",
            "Content-Encoding": "gzip",
            "apikey": self.api,
        }
        response = requests.get(url=endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["id"]
        return code



