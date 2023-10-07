#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch



data = DataManager().load_data()



for data_strings in data:
    try:
        # print(data_strings)
        result_data = FlightSearch().search(data_strings)
        # print(result_data)
        result_dict = FlightData().make_data(result_data)
        # print(result_dict)
        put_data = DataManager().put_data(result_dict)

    except:
        pass







