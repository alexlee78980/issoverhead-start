import requests
from datetime import datetime
import time
import smtplib
MY_LAT = -37 # Your latitude
MY_LONG = 44 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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
time_now = datetime.now()

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if not(sunrise <= time_now.hour <= sunset) and abs(iss_latitude - MY_LAT) > 5 and abs(iss_longitude- MY_LONG) > 5:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="alexleetest123@gmail.com", password="testpassword@123")
            connection.sendmail(from_addr="alexleetest123@gmail.com", to_addrs="alexleetest123@yahoo.com", msg="Subject:Look Up \n\n The ISS is above you!")
    time.sleep(60)




