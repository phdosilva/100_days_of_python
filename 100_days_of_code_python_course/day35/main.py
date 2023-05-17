import requests
# import os
from config import APPID, ACCOUNT_SID, AUTH_TOKEN
from twilio.rest import Client

lat = -8.038572
lon = -34.946235

# account_sid = os.environ["ACCOUNT_SID"]
# auth_token = os.environ.get("AUTH_TOKEN")
# To create environment variable you can do by typing "export VARIABLE=VALUE"

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

params = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "appid": APPID
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()


def will_rain(weather):
    for data in weather:
        for item in data["weather"]:
            if "id" in item and item["id"] < 700:
                return True
    return False


if will_rain(response.json()["hourly"][:12]):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's gonna rain! 🌧🌧🌧",
        from_='+16292059209',
        to='+5581979050331'
    )
    print(message.status, message.sid)
