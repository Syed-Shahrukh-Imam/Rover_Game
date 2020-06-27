from tile import Tile
from rover import Rover
from planet import Planet
import os


def error_printer():
    print()
    print("Unable to load level")
    print()

    return


def load_level(filename):
    """
	Loads the level and returns an object of your choosing
	"""
    if not os.path.isfile(filename):
        print()
        print("Level file could not be found")
        print()

    level_tiles = []  # an array of the tiles of the for the planet.
    name = ""
    width = 0
    height = 0
    rover_positions = []

    # These values are to read from the level file and then updated.
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            line_list = line.split(",")

            if line_list[0] == "name":
                name = line_list[1]
            elif line_list[0] == "width":
                width = int(line_list[1])
            elif line_list[0] == "height":
                height = int(line_list[1])
            elif line_list[0] == "rover":
                rover_positions = [int(line_list[1]), int(line_list[2])]
            elif line_list[0] == "plains" or line_list[0] == "shaded":
                if line_list[0] == "shaded":
                    shaded = True
                else:
                    shaded = False

                high_elevation = int(line_list[1])
                if len(line_list) == 2:
                    low_elevation = high_elevation

                tile = Tile(shaded, high_elevation, low_elevation)
                level_tiles.append(tile)

    if name == "" or width == -1 or height == -1 or len(rover_positions) == 0:
        return error_printer()

    if width < 5 or height < 5:
        return error_printer()

    x, y = rover_positions

    if x < 0 or x >= width or y < 0 or y >= height:
        return error_printer()

    if len(level_tiles) != height * width:
        return error_printer()

    tiles = []

    for n in range(0, width):
        tiles.append( [None] * height )

    i = 0
    j = 0

    for tile in level_tiles:
        tiles[i][j] = tile

        if i == width - 1:
            i = 0
            j += 1
        else:
            i += 1

    rover = Rover(x, y)
    planet = Planet(name, width, height, tiles, rover)
