import requests
from datetime import datetime
import time
import smtplib

# my position
MY_LAT = 53.551086 # Your latitude
MY_LONG = 9.993682 # Your longitude

# email configuration
EMAIL = "mail@mail.me"
PASSWORD = "empty"
SMTP = "smtp.nowhere.me"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["result"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["result"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    # if is_iss_overhead() and is_night():
        # with (smtplib.SMTP(SMTP)) as connection:
        #     connection.starttls()
        #     connection.login(EMAIL, PASSWORD)
        #     connection.sendmail(
        #         from_addr=EMAIL,
        #         to_addrs=EMAIL,
        #         msg="Subject: Look Up! \n\n The ISS is above you in the sky"
        #     )
    # for local testing without sending an email
    if is_iss_overhead():
        print("Look up, it's out there")
    else:
        print("Nothing to see here, move on..")
