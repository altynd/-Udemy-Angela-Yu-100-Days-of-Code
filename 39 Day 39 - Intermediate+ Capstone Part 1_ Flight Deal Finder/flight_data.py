
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        pass

    def make_data(self,flight_data_min):

        flight_data_dict = {
            "price_min": flight_data_min["price"],
            "city_from": flight_data_min["cityFrom"],
            "code_from": flight_data_min["cityCodeFrom"],
            # "city_to": flight_data_min["cityTo"],
            "code_to": flight_data_min["cityCodeTo"],
            "datetime": flight_data_min["local_departure"],
        }
        return flight_data_dict
