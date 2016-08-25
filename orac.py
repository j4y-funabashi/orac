#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, dirname
from os import environ
from dotenv import load_dotenv


import requests

def get_weather(api_url, city, api_key):
    url = "%s/weather?q=%s&units=metric&appid=%s" % (api_url, city, api_key)
    weather = requests.get(url).json()
    out = "%s %sC" % (weather['weather'][0]['main'], weather['main']['temp'])
    print(out)



dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_url = "http://api.openweathermap.org/data/2.5"
city = "Leeds,uk"
api_key = environ.get("WEATHER_API_KEY")
get_weather(api_url, city, api_key)
