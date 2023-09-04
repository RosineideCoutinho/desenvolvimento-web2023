#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importing necessary libraries
import requests
import json
# Function to get weather data
def get_weather(city):
try:
# Url for fetching weather data
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&amp;appid=7dfc6f0f9f9f6cc7fd4a324b45f2c130"
# Getting response from the url
response = requests.get(url)
# Converting response to json format
weather_data = json.loads(response.text)
# Getting relevant data
temperature = int(weather_data['main']['temp'] - 273.15)
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
description = weather_data['weather'][0]['description']
country = weather_data['sys']['country']
