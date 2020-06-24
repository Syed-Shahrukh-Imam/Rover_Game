class Rover:

    def __init__(self, x, y):
        """
		Initialises the rover
		"""
        self.x = x
        self.y = y
        self.battery = 100

    def get_coordinates(self):
        return self.x, self.y

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y
