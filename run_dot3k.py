#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dot3k.menu import MenuOption
import orac

class BusTimes(MenuOption):

    def __init__(self):
        self.output = [
                {"text": "yo"},
                {"text": "yo"},
                {"text": "yo"}
                ]
        self.last_update = 0
        self.update_interval = 300
        MenuOption.__init__(self)

    def update(self):

        if self.millis() - self.last_update < 1000 * self.update_interval:
            return False

        self.last_update = self.millis()

        stop_atco_code = "450010861"
        api_url = "http://transportapi.com/v3/uk/bus/stop"
        app_id = ""
        app_key = ""
        times = orac.get_bus_times(stop_atco_code, app_id, app_key, api_url)
        self.output[0]["text"] = times[0]
        self.output[1]["text"] = times[1]
        self.output[2]["text"] = times[2]

    def redraw(self, menu):
        self.update()

        menu.write_option(
            row=0,
            margin=1,
            text=self.output[0]["text"]
        )
        menu.write_option(
            row=1,
            margin=1,
            text=self.output[1]["text"]
        )
        menu.write_option(
            row=2,
            margin=1,
            text=self.output[2]["text"]
        )


import dot3k.joystick as joystick
import dot3k.lcd as lcd
from dot3k.menu import Menu
import time

menu = Menu({
        'BusTimes': BusTimes()
    },
    lcd,  # Draw to dot3k.lcd
)

REPEAT_DELAY = 0.5

@joystick.on(joystick.UP)
def handle_up(pin):
    menu.up()
    joystick.repeat(joystick.UP, menu.up, REPEAT_DELAY, 0.9)

@joystick.on(joystick.DOWN)
def handle_down(pin):
    menu.down()
    joystick.repeat(joystick.DOWN, menu.down, REPEAT_DELAY, 0.9)

@joystick.on(joystick.LEFT)
def handle_left(pin):
    menu.left()
    joystick.repeat(joystick.LEFT, menu.left, REPEAT_DELAY, 0.9)

@joystick.on(joystick.RIGHT)
def handle_right(pin):
    menu.right()
    joystick.repeat(joystick.RIGHT, menu.right, REPEAT_DELAY, 0.9)

@joystick.on(joystick.BUTTON)
def handle_button(pin):
    menu.select()

while 1:
    # Redraw the menu, since we don't want to hand this off to a thread
    menu.redraw()
    time.sleep(0.05)
