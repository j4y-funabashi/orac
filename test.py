#!/usr/bin/env python

import dot3k.lcd as lcd
import dot3k.backlight as backlight

backlight.rgb(255, 255, 255)
lcd.clear()
lcd.write("Hello World")
