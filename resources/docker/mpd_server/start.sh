#!/bin/bash

mpdscribble --no-daemon --verbose
mpd --no-daemon --stdout -v /etc/mpd.conf
