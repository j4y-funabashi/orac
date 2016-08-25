#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_weather(api_url, city, api_key):
    url = "%s/weather?q=%s&units=metric&appid=%s" % (api_url, city, api_key)
    print url




api_url = "http://api.openweathermap.org/data/2.5"
city = "Leeds,uk"
api_key = ""
get_weather(api_url, city, api_key)
