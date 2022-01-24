import requests

API_KEY = "bba9f8e206207be6580401c9828126d8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city  = input("Enter City name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather']
    temperature = data["main"]["temp"] - 273.15
    print(round(temperature * (9/5) + 32), "F")
else:
    print("Error")