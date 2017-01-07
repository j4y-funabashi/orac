from dot3k.menu import MenuOption

class Radio(MenuOption):

    def __init__(self):
        MenuOption.__init__(self)

    def redraw(self, menu):
        menu.write_option(
                row=1,
                margin=1,
                icon="",
                text="Play"
                )
        menu.write_option(
                row=2,
                margin=1,
                icon="",
                text="Stop"
                )
        menu.clear_row(0)
