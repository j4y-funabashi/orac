#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dot3k.menu import MenuOption

class BusTimes(MenuOption):

    def __init__(self):
        MenuOption.__init__(self)

    def redraw(self, menu):
        print("cheese!")
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
    time.sleep(0.01)
