import requests
from datetime import datetime
my_lat = 41.8781
my_long = 87.6298

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data) # {'message': 'success', 'iss_position': {'latitude': '- 35', 'longitude': '-39'}, 'timestamp': 1639603348}

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
iss_position = (latitude,longitude)
print(iss_position)


parameters = {
    "lat" : my_lat,
    "lng" :my_long,
    "formatted" : 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise.split('T')[1].split(":")[0])
timenow = datetime.now()
print(timenow)