import requests
from weather_data import weather_data

API_WEATHER = "eef30f470de921df5269e4f20a154b51"

link = "https://api.openweathermap.org/data/2.5/onecall"


params = {
    "lat":71,
    "lon":73.8,
    "exclude": "current,minutely,daily",
    "appid":API_WEATHER
}

try:
    response = requests.get(link,params=params)
    response.raise_for_status()
    weather_data = response.json()
except:
    weather_data=weather_data

# for hours 0-11
# if code <700 then using umbrella

#weeather in 12 hours
weather_hourly = weather_data["hourly"][:12]
is_rain = False
for each_hour in weather_hourly:
    if each_hour["weather"][0]["id"] < 700:
        is_rain = True

if is_rain:
    print("it is rain")

