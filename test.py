#!/usr/bin/env python

import sys
import time

import dot3k.backlight as backlight
import dot3k.joystick as nav
import dot3k.lcd as lcd
from dot3k.menu import Menu, MenuOption

from clock import Clock

class Radio(MenuOption):

    def __init__(self):
        MenuOption.__init__(self)

    def redraw(self, menu):
        menu.write_option(
                row=1,
                margin=1,
                icon=">",
                text="Radio stuff"
                )
        menu.clear_row(0)
        menu.clear_row(2)

class Status(MenuOption):

    def __init__(self):
        MenuOption.__init__(self)

    def redraw(self, menu):
        menu.write_option(
                row=1,
                margin=1,
                icon=">",
                text="Status stuff"
                )
        menu.clear_row(0)
        menu.clear_row(2)

backlight.rgb(255, 255, 255)

menu = Menu({
        'Clock': Clock(),
        'Radio': Radio(),
        'Status': Status(),
    },
    lcd,
    Status(),
    30)

"""
You can use anything to control dot3k.menu,
but you'll probably want to use dot3k.joystick
"""
REPEAT_DELAY = 0.5


@nav.on(nav.UP)
def handle_up(pin):
    menu.up()
    nav.repeat(nav.UP, menu.up, REPEAT_DELAY, 0.9)


@nav.on(nav.DOWN)
def handle_down(pin):
    menu.down()
    nav.repeat(nav.DOWN, menu.down, REPEAT_DELAY, 0.9)


@nav.on(nav.LEFT)
def handle_left(pin):
    menu.left()
    nav.repeat(nav.LEFT, menu.left, REPEAT_DELAY, 0.9)


@nav.on(nav.RIGHT)
def handle_right(pin):
    menu.right()
    nav.repeat(nav.RIGHT, menu.right, REPEAT_DELAY, 0.9)


@nav.on(nav.BUTTON)
def handle_button(pin):
    menu.select()


while 1:
    menu.redraw()
    time.sleep(0.05)
