#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_weather(api_url, city, api_key):
    url = "%s/weather?q=%s&units=metric&appid=%s" % (api_url, city, api_key)
    weather = requests.get(url).json()
    return "%s %sC" % (weather['weather'][0]['main'], weather['main']['temp'])
