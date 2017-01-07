#!/usr/bin/env python

import time

import dot3k.backlight as backlight
import dot3k.joystick as nav
import dot3k.lcd as lcd
from dot3k.menu import Menu, MenuOption

from radio import Radio
from status import Status

backlight.rgb(255, 255, 255)


menu = Menu({
        'Radio': Radio(),
        'Status': Status()
    },
    lcd,
    Status(),
    30)


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
