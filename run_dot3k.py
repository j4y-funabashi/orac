#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dot3k.menu import MenuOption

class Playlist(MenuOption):

    def __init__(self):
        self.selected_option = 0
        self.options = []
        MenuOption.__init__(self)

    def redraw(self, menu):
        menu.write_option(
            row=0,
            margin=1,
            icon='>',
            text="Playlist"
        )

        print(self.millis())


import dot3k.joystick as joystick
import dot3k.lcd as lcd
from dot3k.menu import Menu
import time

menu = Menu({
        'Music': {
            'Playlist': Playlist()
        },
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
