#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dot3k.menu import MenuOption

class HelloWorld(MenuOption):

    def redraw(self, menu):
        menu.write_option(
                row=1,
                text='Hello World! How are you today?',
                scroll=True
                )

        menu.clear_row(2)


from dot3k.menu import Menu
import dot3k.backlight
import dot3k.lcd
import time

dot3k.backlight.rgb(255, 255, 255)

menu = Menu(
        structure={
            'Hello World': HelloWorld()
            },
        lcd=dot3k.lcd
        )

menu.right()

while 1:
    menu.redraw()
    time.sleep(0.01)
