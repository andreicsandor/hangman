# Variable used to clear terminal
# Replace with "cls" for Windows OS
CLEAR = "clear"

# Number of lives per Hangman round
MAX_LIFE = 7

# Number of rounds
ROUNDS = 3

# Wordnik API
KEY = "a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"

# Size of requested words sample
LIMIT = 50

# Waiting times
SHORT_TIME = 0.5
MEDIUM_TIME = 0.75
LONG_TIME = 1


def main():

    # Boots up the game console
    name, game = boot_console()

    # Starts the game
    if game == "1" or game == "2":
        load_hangman(name)


def validate_name(name):
    """Validates the user's name."""

    if 10 >= len(name) >= 4 and name.isalnum():
        return True
    else:
        return False


def printer_bold(object):
    """Displays bolded messages."""

    # Prints message
    print("\033[1m" + object + "\033[0m")


def printer_reverse(object):
    """Displays messages in the terminal using reversed motion effect."""

    # Prints the message
    for step in reversed(range(len(object))):
        time.sleep(SHORT_TIME)
        os.system(CLEAR)
        # Enables the transition effect
        for line in reversed(range(len(object) - step)):
            printer_bold(object[line])