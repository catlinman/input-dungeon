
# File containing helper functions used throughout the project.
# Loop helper function.

def loop(v, min, max):
	if v < min: return max
	elif v > max: return min
	else: return v