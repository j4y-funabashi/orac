#!/bin/bash

mpdscribble --no-daemon --verbose 2
mpd --no-daemon --stdout -v /etc/mpd.conf
