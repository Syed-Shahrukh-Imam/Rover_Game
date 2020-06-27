
class Planet:
	def __init__(self, name, width, height, tiles, rover):
		"""
		Initialise the planet object
		"""
		self.name = name
		self.width = width
		self.height = height
		self.tiles = tiles
		self.rover = rover # A planet has a rover instance.
		x,y = rover.get_coordinates()

	def get_rover(self):
		return self.rover

	def get_percent_explored(self):
		num_explored = 0
		for x in range(0, self.width):
			for y in range(0, self.height):
				if self.tiles[x][y].get_explored():
					num_explored += 1
		return int(num_explored / (self.width * self.height) * 100)

	def get_name(self):
		return self.name

	def find_tile(self, x, y):
		return self.tiles[x % self.width][y % self.height]

	
	




