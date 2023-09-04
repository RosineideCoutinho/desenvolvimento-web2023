
import data as data


import icon as icon
import requests

import json
import urllib3
import document






from climate1.scripts.climate import searchBtn, cityInput, windElement, cityElement, tempElement, descElement, \
    weatherIconElement, humidityElement

# Variáveis e selecção de elementos
apikey = 'a6cf52a7b220498046a56aca5754e809'
apiCountryURL = 'https://flagsapi.com/BE/flat/64.png'
city_input = document.querySelector('#city-input')
search_btn = document.querySelector('#search')
city_element = document.querySelector('#city')
temp_element = document.querySelector('#temperature span')
desc_element = document.querySelector('#description')
weather_icon_element = document.querySelector('#weather-icon')
country_element = document.querySelector('#acoutry')
humidity_element = document.querySelector('#umidity')
wind_element = document.querySelector('#wind span')
# Funções
# Funções

def getweatherDate(city):
apiweatherURL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&amp;units=metric&amp;appid={apikey}&amp;lang-pt'

res = requests.get(apiweatherURL)
date = res.json()

print(date)


def showWeatherDate(city):
date = getweatherDate(city)

cityElement.innerText = date['name']
tempElement.innerText = int(date['main']['temp'])
descElement.innerText = date['weather'][0]['description']
weatherIconElement.setAttribute("src", f'http://openweathermap.org/img/wn/{date["weather"][0]["icon"]}.png')

humidityElement.innerText = f"{date['main']['humidity']}%"
windElement.innerText = f"{date['wind']['speed']}km/h"

#Eventos
def clickEvent(e):
e.preventDefault()

city = cityInput.value
print("teste")

searchBtn.addEventListener("click", clickEvent)

