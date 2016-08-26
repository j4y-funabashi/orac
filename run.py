#!/usr/bin/env python
# -*- coding: utf-8 -*-

import orac

from dotenv import load_dotenv, find_dotenv
from os import environ
import time


# print(orac.get_mpd_playlist())

load_dotenv(find_dotenv())
api_url = "http://api.openweathermap.org/data/2.5"
city = "Leeds,uk"
api_key = environ.get("WEATHER_API_KEY")
# print(orac.get_weather(api_url, city, api_key))


stop_atco_code = "450010861"
api_url = "http://transportapi.com/v3/uk/bus/stop"
app_id = environ.get("BUS_APP_ID")
app_key = environ.get("BUS_APP_KEY")
times = orac.get_bus_times(stop_atco_code, app_id, app_key, api_url)
print(times[0])
print(times[1])
print(times[2])
