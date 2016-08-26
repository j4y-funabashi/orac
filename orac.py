#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from mpd import MPDClient

def get_weather(api_url, city, api_key):
    url = "%s/weather?q=%s&units=metric&appid=%s" % (api_url, city, api_key)
    weather = requests.get(url).json()
    return "%s %sC" % (weather['weather'][0]['main'], weather['main']['temp'])

def get_bus_times(stop_atco_code, app_id, app_key, api_url):
    url = "%s/%s/live.json?app_id=%s&app_key=%s&group=no&nextbuses=yes" % (api_url, stop_atco_code, app_id, app_key)
    bus_times = requests.get(url).json()
    return ["{0[aimed_departure_time]} {0[line]} {0[direction]}".format(bus) for bus in bus_times['departures']['all']]

def get_mpd_playlist():
    client = MPDClient()
    client.timeout = 10
    client.connect("localhost", 6600)
    current_song = "> {0[artist]} - {0[title]}".format(client.currentsong())
    next_song = "{0[artist]} - {0[title]}".format(client.playlistid(client.status()['nextsongid']).pop())
    client.close()
    client.disconnect()
    return [current_song, next_song]
