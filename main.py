import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""

parameters = {
    "lat": "Latitude",
    "lon": "Longitude",
    "exclude": "current,minutely,daily",
    "appid": "",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly = weather_data["hourly"]

want_data = [weather_data["hourly"][hour_id]["weather"][0]["id"] for hour_id in range(12)]
will_rain = False
for current_id in want_data:
    if current_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
                body="It's going to rain today. Remember to bring an Umbrella ☔",
                from_="no.",
                to="receiver no."
                )

    print(message.status)
