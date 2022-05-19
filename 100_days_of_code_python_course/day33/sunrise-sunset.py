import requests
import datetime

params = {
    "lat": 26.7201600,
    "lng": -4.4203400,
    "formatted": 0
}

res = requests.get("https://api.sunrise-sunset.org/json", params=params)
res.raise_for_status()
data = res.json()
print(data["results"]["sunset"])

now = datetime.datetime.now()
print(now)





