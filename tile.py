class Tile:

	def __init__(self, shaded, high_elevation, low_elevation ):
		"""
		Initialises the terrain tile and attributes
		"""
		self.shaded = shaded
		self.high_elevation = high_elevation
		self.low_elevation = low_elevation
		self.explored = False  #Initially a tile is marked as unexplored.


	def get_explored(self):
		return self.explored


	def make_explored(self):
		self.explored = True

	def max_elev(self):
		return self.high_elevation

	def min_elev(self):
		return self.low_elevation

	def is_shaded(self):
		return self.shaded
