import requests

response = requests.get(url="http://api.open-notify.org/iss-now")
response.raise_for_status()

data = response.json()["iss_position"]
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

