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
    print(bus_times["request_time"])
    print(bus_times["stop_name"])
    for bus in bus_times['departures']['all']:
        print((bus['aimed_departure_time'], bus['expected_departure_time'], bus['best_departure_estimate'], bus['line'], bus['direction']))

def get_mpd_playlist():
    client = MPDClient()
    client.timeout = 10
    client.connect("localhost", 6600)
    current_song = "> %s - %s" % (client.currentsong()['artist'], client.currentsong()['title'])
    next_song = client.playlistid(client.status()['nextsongid']).pop()
    next_song = "%s - %s" % (next_song['artist'], next_song['title'])
    print(current_song)
    print(next_song)
    client.close()
    client.disconnect()
