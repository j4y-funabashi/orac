from dot3k.menu import MenuOption

import time

class Status(MenuOption):

    def __init__(self):
        MenuOption.__init__(self)

    def redraw(self, menu):
        menu.write_option(
                row=1,
                margin=1,
                icon="",
                text=time.strftime(' %a %H:%M:%S ')
                )
        menu.clear_row(0)
        menu.clear_row(2)
