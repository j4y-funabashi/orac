#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dot3k.lcd as lcd
import time
import orac

def redraw():
    times = orac.get_bus_times(stop_atco_code, app_id, app_key, api_url)
    lcd.set_cursor_position(0, 0)
    lcd.write(times[0])
    lcd.set_cursor_position(0, 1)
    lcd.write(times[1])
    lcd.set_cursor_position(0, 2)
    lcd.write(times[2])

redraw()
