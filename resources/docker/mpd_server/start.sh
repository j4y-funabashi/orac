#!/bin/bash

mpd --no-daemon --stdout -v /etc/mpd.conf
mpdscribble --no-daemon --verbose 2
