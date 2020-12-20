import requests
import os
import twilio.rest as client

# api and auth key should go to env variables so this is how to get them. os package needed for this to work
auth_key = os.environ.get("AUTH_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
api_key = os.environ.get("OWM_APIKEY")

# twilio configuration
# account_sid = "account_sid_string"
# auth_token = "auth_token_string"

# open weather map configuration
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": "53.549999",
    "lon": "10.01667",
    "exclude": "current,minutely,daily",
    "units": "metric",
    "lang": "de",
    "appid": api_key,
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
current_data = response.json()

weather_slice = current_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print("Bring an Umbrella")
    client = client(account_sid, auth_token)
    message = client.messages \
        .create(
            body='It may rain today. Bring an umbrella',
            from_='twilio_number_goes_here',
            to='my_verified_number'
        )

    # print message status ( should be queued )
    print(message.status)


