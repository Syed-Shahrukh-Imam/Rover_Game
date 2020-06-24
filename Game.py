import sys


def main_menu():
    """This function starts the game and prints out the menu
    for the user. The user then enters the level he wants to play."""

    print("************WELCOME TO THE ROVER GAME! TIME TO EXPLORE A PLANET************")


    # Users can enter START <level>, HELP, or Quit

    while True:
        user_input = input("Your command sire: ")
        if user_input == "START":
            start_game(user_input.split()[1])
        elif user_input == "HELP":
            help_menu()
        elif user_input == "QUIT":
            quit_the_game()
        else:
            print("Invalid Command. TRY AGAIN!!!")

def start_game( level_filename ):
    """
    :param level_filename:

    The level file is read and the game is played by the user.
    """

    print("The level has started.")

def help_menu():
    """
    :return: void
    The help menu of the game is printed for the user
    """
    print("""
    START : This commands starts the level. You need to pass in the level file you want to play
    HELP : Shows the help menu
    QUIT : Quits the game.
    """)

def quit_the_game():
    sys.exit(0)



main_menu()
