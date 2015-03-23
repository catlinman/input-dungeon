
# Main terminal interaction script. Works as an I/O and program flow handling layer to make the main code look cleaner.

import re
import os
import sys
import time

# Takes in a dictinary and returns a formatted string of the dictonary's keys.
def __keys_to_string(d):
	s = "" # Output variable.
	l = len(d) # Number of entries.
	i = 0 # Iteration index.

	# Iterate over the keys and add them to the output variable.
	for key, value in d.items():
		if l > 1:
			if i == 0:
				s = s + ("%s" % key)

			else:
				s = s + (" | %s" % key)

			i = i + 1

		else:
			s = key

	return s

# These lambda functions act as short names for some functions used throughout the code.
clear = lambda: os.system('cls') # Make the terminal clear command nicer to use by assigning it to a short variable.
clearline = lambda: sys.stdout.write("\r%s" % (" " * (__width - 1)))
wait = lambda x: time.sleep(x)
write = lambda x: sys.stdout.write(x)

# Function to simply output a string to the terminal. If ignore is True the output will not receive a new line at the end.
def output(message = "Output", ignore = False):
	sys.stdout.write(message)

	if ignore == False:
		sys.stdout.write("\n")

	sys.stdout.flush()

# Function to output a string per character at a given speed (in seconds). If ignore is True the output will not receive a new line at the end.
def outputbuild(message = "Output", speed = 0.01, ignore = False):
	# Variable containing the current section of the string to build. We also strip all control characters.
	splitmessage = re.compile(r'[\n\r\t]').sub(" ", message)

	index = 0 # Index of the current build character in the split message.
	output = "" # Output string that is gradually printed to the console.

	# Make sure that the split message is not empty and that the index is not greater than the actual string.
	while len(splitmessage) > 0 and index < len(splitmessage):
		output = output + splitmessage[index] # Build one character.

		sys.stdout.write("\r%s" % output) # Write the current string build.

		time.sleep(speed) # Sleep the thread for the given amount of time.

		# Split the string if it is too large to print in a single line. This prevents the terminal from going haywire.
		if index == __width - 1:
			splitmessage = splitmessage[index + 1:] # Fetch the next segment to print.
			output = "" # Reset the output since a new line is being printed.
			index = 0 # Reset the index since the string now starts from zero again.

		else:
			index = index + 1 # Increment the index.

	if ignore == False:
		sys.stdout.write("\n")

	sys.stdout.flush()

# Asks for user input and returns the entered value. Just a simple wrapper for raw_input.
def input(message = "Input: "):
	if message:
		output(message)

	return raw_input("> ")

# Same as input but with the input message being built instead.
def inputbuild(message = "Input: ", speed = 0.01):
	if message:
		outputbuild(message, speed)

	return raw_input("> ")

# Asks the user to enter a message matching the name of a key in the command dictionary. If hint is True the console will print the possible commands.
# Note: Requires the command dictionary to contain function references.
def command(message = "", commands = {}, verbose = False):
	if len(commands) > 0: # Make sure that the command dictionary is not empty.
		selected = False # Stores the state of user interaction. Is True if the user selected a valid command.

		while not selected:
			if message:
				output(message)

			if verbose:
				output("(Commands: %s)" % __keys_to_string(commands))

			s = raw_input("> ") # Get user input.

			try:
				if commands[s]:

					commands[s]() # Execute the command and set selected to True.
					selected = True

			except KeyError:
				pass

	else:
		output("Terminal: The command list supplied does not contain any values.")

# Same as command but with building strings.
def commandbuild(message = "", commands = {}, verbose = False, speed = 0.01):
	if len(commands) > 0: # Make sure that the command dictionary is not empty.
		selected = False # Stores the state of user interaction. Is True if the user selected a valid command.

		while not selected:
			if message:
				outputbuild(message, speed)

			if verbose:
				outputbuild("- %s -" % __keys_to_string(commands), speed)

			s = raw_input("> ") # Get user input.

			try:
				if commands[s]:

					commands[s]() # Execute the command and set selected to True.
					selected = True

			except KeyError:
				pass

	else:
		output("Terminal: The command list supplied does not contain any values.")

# Function to determine the size of the current terminal window.
def size():
	env = os.environ

	def ioctl_GWINSZ(fd):
		try:
			import fcntl, termios, struct, os
			cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
		except:
			return
		return cr

	cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)

	if not cr:
		try:
			fd = os.open(os.ctermid(), os.O_RDONLY)
			cr = ioctl_GWINSZ(fd)
			os.close(fd)

		except:
			pass

	if not cr:
		cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

	return int(cr[1]), int(cr[0])

__width, __height = size() # Terminal size required by some functions.
