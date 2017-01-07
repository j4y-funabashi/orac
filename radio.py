from dot3k.menu import MenuOption

class Radio(MenuOption):

    def __init__(self):
        self.selected_option = 0
        self.options = [
                'Play',
                'Pause'
                ]

        MenuOption.__init__(self)

    def next_option(self):
        self.selected_option = (self.selected_option + 1) % len(self.options)

    def prev_option(self):
        self.selected_option = (self.selected_option - 1) % len(self.options)

    def up(self):
        self.prev_option()

    def down(self):
        self.next_option()

    def get_current_option(self):
        return self.options[self.selected_option]

    def get_next_option(self):
        return self.options[(self.selected_option + 1) % len(self.options)]

    def get_prev_option(self):
	return self.options[(self.selected_option - 1) % len(self.options)]

    def redraw(self, menu):
	menu.write_option(
		row=0,
		margin=1,
		text=self.get_prev_option()
		)

	menu.write_option(
		row=1,
		margin=1,
		icon='>',
		text=self.get_current_option()
		)

	menu.write_option(
		row=2,
		margin=1,
		text=self.get_next_option()
		)
