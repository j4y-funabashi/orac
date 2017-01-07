from dot3k.menu import MenuOption

import orac

class Radio(MenuOption):

    def __init__(self):
        self.selected_option = 0
        self.options = [
                {'title': 'Play', 'action': self.handle_play, 'icon': ' '},
                {'title': 'Stop', 'action': self.handle_stop, 'icon': ' '}
                ]

        MenuOption.__init__(self)

    def up(self):
        self.prev_option()

    def down(self):
        self.next_option()

    def right(self):
        self.select_option()

    def next_option(self):
        self.selected_option = (self.selected_option + 1) % len(self.options)

    def prev_option(self):
        self.selected_option = (self.selected_option - 1) % len(self.options)

    def select_option(self):
        self.options[self.selected_option]['action']()

    def get_current_option(self):
        return self.options[self.selected_option]['title']

    def get_next_option(self):
        return self.options[(self.selected_option + 1) % len(self.options)]['title']

    def get_prev_option(self):
	return self.options[(self.selected_option - 1) % len(self.options)]['title']

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

    def handle_play(self):
        orac.load_radio()

    def handle_stop(self):
        orac.stop_radio()
