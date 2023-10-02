# import requests
# import json
# import os
#
# file_exists = os.path.exists("data.json")
#
# #если файл есть открыть
# if file_exists:
#     with open("data.json", "r") as file:
#         data = json.load(file)
#         latitude = data["iss_position"]["latitude"]
#         longitude = data["iss_position"]["longitude"]
#         location = (latitude, longitude)
#
# #если файла нет скачать
# else:
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     data = response.json()
#     with open("data.json", "w") as file:
#         json.dump(data, file, indent=4)
#
# params = {
#     "lat":latitude,
#     "lng":longitude,
#     "formatted":0
# }
# response_wether =  requests.get("https://api.sunrise-sunset.org/json",params=params)
# response_wether.raise_for_status()
# data_weather = response_wether.json()
# # print(data_weather)
# sunrise_time = data_weather['results']['sunrise']
# sunset_time = data_weather['results']['sunset']
#
# from datetime import datetime
# now_time = datetime.now().isoformat()
#
# sunrise_time = sunrise_time[11:13]
# # #variant_1
# # now_time = now_time.split("T")[1].split(":")[0]
# #variant_2
# now_time = now_time[11:13]
#
# print(sunrise_time)
# print(now_time)
# # 2023-09-29T16:08:49+00:00
# # 2023-09-29T13:09:58.505705
# print(int(sunrise_time)-int(now_time))
#
