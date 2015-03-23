
import terminal

if __name__ == "__main__":
	terminal.clear() # Clear the console screen.

	# Example user interaction for dummies. This should go in some extra file since it's crap code otherwise.
	terminal.outputbuild("Welcome to Input Dungeon")
	terminal.wait(0.25)

	# Temporary command dictionary.

	terminal.commandbuild("Please enter one of the given commands: ", {
		"help": (lambda: terminal.outputbuild("You can enter random things here how wonderful.")),
		"move": (lambda: terminal.commandbuild("Where do you want to move to?", {
			"forward": (lambda: terminal.outputbuild("You move forward.")),
			"left": (lambda: terminal.outputbuild("You move left.")),
			"right": (lambda: terminal.outputbuild("You move right."))
		}, True))
	}, True)