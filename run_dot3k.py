#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dot3k.menu import MenuOption

class Orac(MenuOption):

    def __init__(self):
        self.selected_option = 0
        self.options = [
                {"title": "Next Bus", "action": self.handle_nextbus, "icon": " "}
                ]
        MenuOption.__init__(self)
