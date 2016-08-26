#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dot3k.lcd as lcd
import time
from orac import get_bus_times

def redraw():
    stop_atco_code = "450010861"
    api_url = "http://transportapi.com/v3/uk/bus/stop"
    app_id = environ.get("BUS_APP_ID")
    app_key = environ.get("BUS_APP_KEY")

    times = get_bus_times(stop_atco_code, app_id, app_key, api_url)
    lcd.set_cursor_position(0, 0)
    lcd.write(times[0])
    lcd.set_cursor_position(0, 1)
    lcd.write(times[1])
    lcd.set_cursor_position(0, 2)
    lcd.write(times[2])

redraw()
