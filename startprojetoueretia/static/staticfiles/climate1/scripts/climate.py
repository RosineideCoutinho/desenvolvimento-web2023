
# Variáveis e seleção de elementos
apikey = 'a6cf52a7b220498046a56aca5754e809'
apiCountryURL = 'https://flagsapi.com/BE/flat/64.png'
cityInput = document.querySelector("#city-input")
searchBtn = document.querySelector ("#search")
cityElement = document.querySelector("#city")
tempElement = document.querySelector("#temperature span")
descElement = document.querySelector("#description")
weatherIconElement = document.querySelector("#weather-icon")
countryElement = document.querySelector("#acoutry")
humidityElement = document.querySelector("#humidity")
windElement = document.querySelector("#wind span")

# Funções

# Funções
```python

import requests

def get_weather_date(city):
api_weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&amp;units=metric&amp;appid={apikey}&amp;lang-pt"
res = requests.get(api_weather_url)
date = res.json()
print(date)

def show_weather_date(city):
date = get_weather_date(city)
city_element.innerText = date['name']
temp_element.innerText = int(date['main']['temp'])
desc_element.innerText = date['weather'][0]['description']
weather_icon_element.setAttribute("src", f"http://openweathermap.org/img/wn/{date['weather'][0]['icon']}.png")
humidity_element.innerText = f"{date['main']['humidity']}%"
wind_element.innerText = f"{date['wind']['speed']}km/h"
```
