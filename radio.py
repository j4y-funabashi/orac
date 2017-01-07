from dot3k.menu import MenuOption

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
