#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from mpd import MPDClient

RADIO_FEED_URL = "http://www.radiofeeds.co.uk/bbc6music.pls"
MPD_SERVER = "mpd_server"
MPD_TIMEOUT = 10

def load_radio():
    pls_url = get_playlist_url(RADIO_FEED_URL)

    client = MPDClient()
    client.timeout = MPD_TIMEOUT
    client.connect(MPD_SERVER, 6600)
    client.setvol(100)
    client.clear()
    client.add(pls_url)
    client.play()
    client.close()
    client.disconnect()

    return ""

def stop_radio():
    client = MPDClient()
    client.timeout = MPD_TIMEOUT
    client.connect(MPD_SERVER, 6600)
    client.stop()
    client.close()
    client.disconnect()

    return ""

def get_playlist_url(url):
    result = requests.get(url)
    for l in result.text.split():
        if l.startswith("File1"):
            return l.replace("File1=", "")
