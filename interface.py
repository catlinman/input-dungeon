
# This interface module contains additional behavior for curses to make it more suited for
# the current aim of this project. It enables quick interaction between curses and the
# actual game while still attempting to be flexible and expendable at the same time.

# Developer note: It should be good practice to allow the user to interrupt the program at
# any given point. With that said - there should be checks in place that catch signals
# such as your usual interrupt and actually handle them as expected. This is however not
# automatically the case since curses catches key presses in a raw format, suppressing their
# default behavior and as such completely removing their functionality and use.

import time
import curses
import helpers

NUMUPDATES = 30 # The number of updates per second.
DEBUG = True # Enables development settings to make debugging easier.

# Menu interface class. Creates a scrolling menu inside a specified window.
class Menu:
	def __init__(self, win, x = 0, y = 0):
		self.window = win # The window this menu is attached to.
		self.x, self.y = x, y # Positional offset of the menu.
		self.length = 3 # Maximum number of displayed selections.
		self.inset = 1 # The amount of cells selected items are shifted by.
		
		self.height, self.width = self.window.getmaxyx() # Get the maximum width and height of the assigned window.
		self.selections = [] # Stores the possible selections the user can make.
		self.finished = False # Stores the state of the menu.
		self.cursor = 0 # Current hovered selection index.

	# Add a selection option stored under a specified index. Selections can be overwritten by reassignment to a given index.
	def set_selection(self, item, index):
		# Make sure the option dictionary contains the correct keys. Else replace them with default values.
		if not item.get("desc"):
			item["desc"] = "Menu item"

		if not item.get("out"):
			item["out"] = "None"

		self.selections.append(item) # Append the selection item.

	# Remove a selection by it's key.
	def remove_selection(self, index):
		del self.selections[index]

	# Clear the list of selection.
	def remove_all(self):
		del self.selections[index]

	# Displays the menu and requires input.
	def interact(self):
		self.window.nodelay(1) # Make getch non-blocking.
		self.window.keypad(1) # Enable special keys to return keycodes.

		self.draw() # Draw the current menu.
		self.move(0) # Redraw the cursor to position zero.

		while not self.finished:
			key = self.window.getch() # Get the current pressed keycode. Also, refresh the screen.

			if key == curses.KEY_DOWN: # Arrow down
				self.move(-1)

			elif key == curses.KEY_UP:
				self.move(1)

			elif key == curses.KEY_ENTER or key == 10:
				self.finished = True
				return self.selections[self.cursor]["out"]

			if DEBUG == True:
				if key == 3: exit() # Exit the entire program if the user presses the interrupt key.
				if key == 27: self.finished = True # Exit the menu if the user presses the escape key.

				if key != -1: # Show the keycode.
					self.clearline(self.height - 1)
					self.window.addstr(self.height - 1, self.width - len(str(key)) - 1, str(key))

			time.sleep(1 / NUMUPDATES) # Sleep between checks

	# Draw all menu options/items.
	def draw(self):
		i = 0 # Index variable.
		for opt in self.selections: # Loop over the option items and request them to be drawn.
			self.window.addstr(i + self.y, self.x, "> %s" % opt["desc"])
			i = i + 1

	# Clear a specific line.
	def clearline(self, column):
		self.window.move(column, 0)
		self.window.clrtoeol()

	# Move the current selected line and redraw.
	def move(self, value):
		self.clearline(self.cursor + self.y) # Clear the previously selected line to avoid leftover characters.
		self.cursor = helpers.loop(self.cursor - value, 0, len(self.selections) - 1)
		self.draw() # Redraw the menu to avoid lines from staying selected. 
		self.clearline(self.cursor + self.y) # Clear the line beneath.
		self.window.addstr(self.cursor + self.y, self.x + self.inset, "> %s" % self.selections[self.cursor]["desc"])