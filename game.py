
import time
import curses
import interface

max_x, max_y = 0, 0 # Terminal size variables.
running = True # Determines if the game should continue running or not.

NUMUPDATES = 30 # The number of game updates per second.
DEBUG = True # Enables development settings to make debugging easier.

# Main function supplied to the curses wrapper.
def main(stdscr):
	stdscr.nodelay(1) # Make getch non-blocking.
	stdscr.keypad(1) # Enable special keys to return keycodes.

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
 
	status_window.bkgd(0, curses.color_pair(4)) # Fill the background of the status bar.
	status_window.addstr(1, 1, "Select an item you wish to take on your journey!", curses.color_pair(5))
	status_window.refresh() # Tell the status window to refresh since changes were made.

	start_menu = interface.Menu(game_window, 1, 1) # A simple menu.

	# Add options to the menu. Options are listed in the order they are added.
	start_menu.set_selection({"desc" : "Silver Sword", "out" : "1"}, 1)
	start_menu.set_selection({"desc" : "Crow's Bow", "out" : "2"}, 2)
	start_menu.set_selection({"desc" : "Plated Shield", "out" : "3"}, 3)
	start_menu.set_selection({"desc" : "Staff of Cats", "out" : "4"}, 4)
	start_menu.set_selection({"desc" : "Demon's Charm", "out" : "5"}, 5)
	start_menu.set_selection({"desc" : "Gentleman's Rapier", "out" : "6"}, 6)

	# Show the menu and return the selected choice key to the choice variable.
	out, description = start_menu.interact()
	status_window.clear()

	while running:
		globalkey = stdscr.getch() # Listen for special key presses.

		status_window.bkgd(0, curses.color_pair(4)) # Fill the background of the status bar.
		status_window.addstr(1, 1, "You chose the %s! Press CTRL+C to exit." % description, curses.color_pair(5))
		status_window.refresh()

		if globalkey == 3: exit() # Exit the entire program if the user presses the interrupt key.

		time.sleep(1 / NUMUPDATES) # Sleep the game loop.

# Wrap curses functions in a main function.
curses.wrapper(main)