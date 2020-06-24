from tile import Tile
from rover import Rover
from planet import Planet
import os

def error_printer():
	print()
	print("Unable to load level")
	print()

def load_level(filename):
	"""
	Loads the level and returns an object of your choosing
	"""
	if not os.path.isfile(filename):
		print()
		print("Level file could not be found")
		print()
