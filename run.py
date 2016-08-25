#!/usr/bin/env python
# -*- coding: utf-8 -*-

import orac

from dotenv import load_dotenv, find_dotenv
from os import environ
import time

load_dotenv(find_dotenv())
api_url = "http://api.openweathermap.org/data/2.5"
city = "Leeds,uk"
api_key = environ.get("WEATHER_API_KEY")

while 1:
    print(orac.get_weather(api_url, city, api_key))
    time.sleep(60)
