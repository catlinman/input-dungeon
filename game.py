
import curses
import interface

max_x, max_y = 0, 0 # Terminal size variables.
running = True # Determines if the game should continue running or not.

# Main function supplied to the curses wrapper.
def main(stdscr):
	max_y, max_x = stdscr.getmaxyx() # Save the max screen sizes.

	curses.curs_set(0) # Hide the blinking cursor.

	# Set base colors.
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK) # RED | BLACK
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # GREEN | BLACK
	curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK) # BLUE | BLACK
	curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_WHITE) # WHITE | WHITE
	curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE) # BLACK | WHITE

	# Create base windows.
	status_window 	= curses.newwin(2, 0, 0, 0) # Stores player and game information.
	game_window 	= curses.newwin(0, 0, 2, 0) # Contains the game area.
	# Fill the status window.
	status_window.bkgd(0, curses.color_pair(4)) # Fill the background of the status bar.
	status_window.addstr(1, 1, "Use the arrow keys to navigate and the return key to confirm", curses.color_pair(5))
	status_window.refresh() # Tell the status window to refresh since changes were made.

	# Everything after this point should run within a game loop.
	# Currently since barely any systems are in place we are making a somewhat bastardized game loop here.
	# This means that we are declaring things each loop which you clearly shouldn't do and is only for placeholder purposes.
	while running:
		start_menu = interface.Menu(game_window, 1, 1) # A simple menu.

		# Add options to the menu. Options are listed in the order they are added.
		start_menu.set_selection({"desc" : "This is the first option", "out" : "first"}, 1)
		start_menu.set_selection({"desc" : "This is the second option", "out" : "second"}, 2)
		start_menu.set_selection({"desc" : "This is the last option", "out" : "last"}, 3)

		# Show the menu and return the selected choice key to the choice variable.
		choice = start_menu.interact()
		game_window.clear()

		if choice == "first":
			pass

		elif choice == "second":
			pass

		else:
			pass

# Wrap curses functions in a main function.
curses.wrapper(main)