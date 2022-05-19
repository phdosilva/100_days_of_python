import requests
from datetime import datetime
import smtplib


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

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

time_now = datetime.now()

is_night = time_now.hour > sunset or time_now.hour < sunrise
is_close = abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5

if is_night and is_close:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="gmail.com", password="")
        connection.sendmail(from_addr="gmail.com",
                            to_addrs="@gmail.com",
                            msg="Subject:The ISS is close and you can see!\n\nGo out and look at the sky. ISS is "
                                "passing near you!")



