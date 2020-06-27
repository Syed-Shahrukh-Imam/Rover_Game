import os
from loader import load_level
from planet import Planet

planet = None


def quit_game():
    """
    Will quit the program
    """
    return exit()


def menu_help():
    """
    Displays the help menu of the game
    """
    print("""
START <level file> - Starts the game with a provided file.
QUIT - Quits the game
HELP - Shows this message
""")


def scan_shade(planet):
    """
    Print a 5x5 tile scan around the rover
    """
    print("")
    rover = planet.get_rover()
    centre_x, centre_y = rover.get_coordinates()
    for y in range(centre_y - 2, centre_y + 3):
        symbols = ['']
        for x in range(centre_x - 2, centre_x + 3):
            tile = planet.find_tile(x, y)
            if centre_x == x and centre_y == y:
                symbols.append("H")
            elif tile.is_shaded():
                symbols.append("#")
            else:
                symbols.append(" ")
            tile.make_explored()
        symbols.append('')
        print('|'.join(symbols))

    print("")


def scan_elevation(planet):
    """
    Print a 5x5 tile scan around the rover
    """
    print("")
    rover = planet.get_rover()
    centre_x, centre_y = rover.get_coordinates()
    rover_tile = planet.find_tile(centre_x, centre_y)
    for y in range(centre_y - 2, centre_y + 3):
        symbols = ['']
        for x in range(centre_x - 2, centre_x + 3):
            tile = planet.find_tile(x, y)
            if centre_x == x and centre_y == y:
                symbols.append("H")
            else:
                if rover_tile.max_elev() < tile.min_elev():
                    symbols.append("+")
                elif rover_tile.min_elev() > tile.max_elev():
                    symbols.append("-")
                else:
                    symbols.append(" ")
            tile.make_explored()
        symbols.append('')
        print('|'.join(symbols))

    print("")


def move(planet, direction, cycles):
    rover = planet.get_rover()
    steps_moved = 0
    while steps_moved < cycles:
        # Move the rover one step
        rx, ry = rover.get_coordinates()
        rover_tile = planet.find_tile(rx, ry)
        # work out coordinates for the new tile
        if direction == "N":
            nx = rx
            ny = ry - 1
        elif direction == "S":
            nx = rx
            ny = ry + 1
        elif direction == "W":
            nx = rx - 1
            ny = ry
        else:
            nx = rx + 1
            ny = ry
        new_tile = planet.find_tile(nx, ny)
        if rover_tile.max_elev() < new_tile.min_elev():
            return  # Can't move
        if rover_tile.min_elev() > new_tile.max_elev():
            return  # Can't move
        rover.update_coordinates(nx, ny)
        new_tile.make_explored()
        steps_moved += 1


def menu_start_game(filepath):
    """
    Will start the game with the given file path
    """
    planet = load_level(filepath)
    if planet is None:
        menu()

    while True:
        user_input = input()
        if user_input == "FINISH":
            print("")
            print("You explored {}% of {}".format(planet.get_percent_explored(), planet.get_name()))
            print("")
            return
        elif user_input == "STATS":
            print("DO STATS")
        elif user_input.startswith("MOVE"):
            input_list = user_input.split()
            direction = input_list[1]
            cycles = int(input_list[2])
            move(planet, direction, cycles)
        elif user_input.startswith("WAIT"):
            input_list = user_input.split()
            cycles = int(input_list[1])
            print("DO WAIT")
        elif user_input.startswith("SCAN"):
            if user_input == "SCAN shade":
                scan_shade(planet)
            elif user_input == "SCAN elevation":
                scan_elevation(planet)
            else:
                print("Cannot perform this command")
        else:
            print("Cannot perform this command")


def menu():
    """
    Start the menu component of the game
    """
    planet = None
    running = True
    while running == True:
        user_input = input('')  ## TAKES IN USER INPUT###
        if user_input == 'QUIT' or user_input == 'quit':
            running = False
            quit_game()
        elif user_input == 'HELP' or user_input == 'help':
            menu_help()
        elif user_input.startswith("START") or user_input.startswith('start'):
            input_list = user_input.split()  ###INPUT CONTAINS LEVEL FILE WHICH NEEDS TO BE SEPARATED##
            try:
                menu_start_game(input_list[1])
            except Exception:
                print("")
                print("No level file given")
                print("")
        else:
            print("")
            print("No menu item")
            print("")
            continue


menu()