import requests
from datetime import datetime
MY_LAT = 21.485811
MY_LONG = 39.192505

# response = requests.get(url=)

parameters = {
    "lat" : MY_LAT,
    "lng": MY_LONG,
    "formatted" : 0,
    "tzid" :"Asia/Riyadh"

}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters )
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)