#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import subprocess
import requests

from dot3k.menu import MenuOption

class BusTimes(MenuOption):

    def __init__(self):
        MenuOption.__init__(self)

    def get_bus_times(self):
        result = requests.get('http://bitofahack.com/post/getbusdata.php?stop=45011123')
        return result.json()

    def redraw(self, menu):
        t = datetime.datetime.now().strftime("%H:%M:%S.%f")
        print(t + self.get_bus_times())
        menu.write_option(
                row=1,
                text='Hello World! How are you today?',
                scroll=True
                )


from dot3k.menu import Menu
import dot3k.backlight
import dot3k.lcd
import time

dot3k.backlight.rgb(255, 255, 255)

menu = Menu(
        structure={
            'Bus': BusTimes()
            },
        lcd=dot3k.lcd
        )

menu.right()

while 1:
    menu.redraw()
    time.sleep(60)
