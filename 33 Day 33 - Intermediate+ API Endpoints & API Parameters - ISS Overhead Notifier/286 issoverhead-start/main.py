import requests
from datetime import datetime
import logging
import os

logging.basicConfig(level=logging.DEBUG)
# logging.disable(logging.CRITICAL)

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

logging.debug(iss_latitude)
logging.debug(iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
logging.debug(f"sunrise - {sunrise}")
logging.debug(f"sunset - {sunset}")

time_now = int(datetime.now().isoformat()[11:13]) #15



is_close_to_my_position = False
#If the ISS is close to my current position
if (MY_LAT-iss_latitude) <=5 or (MY_LAT - iss_latitude) >= -5 \
        and (MY_LONG - iss_longitude) <= 5 or (MY_LONG - iss_longitude) >= -5:
    logging.debug("if is_close_to_my_position")
    is_close_to_my_position = True

# time_now = 3
logging.debug(f"time_now - {time_now}") #2023-09-29 15:01:25.942514
# and it is currently dark
is_time_to_sleep = False
if time_now < sunrise or time_now > sunset:
    logging.debug("if is_time_to_sleep")
    is_time_to_sleep = True


# Then send me an email to tell me to look up.
if is_close_to_my_position and is_time_to_sleep:
    import smtplib
    my_email = os.environ.get("my_email")
    my_password = os.environ.get("my_pass")
    smtp = "smtp.gmail.com"
    message = "Subject: Look up!\n\n" \
              "body text"
    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)


# BONUS: run the code every 60 seconds.



