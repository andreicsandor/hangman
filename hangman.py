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


def printer(type, duration, screen=''):
    """Displays messages in the terminal using motion effect."""

    # Displays console loading screen
    # "WELCOME TO CS50 🕹️ STATION"
    # "WANNA PLAY A GAME?"
    # "[1] RED PILL"
    # "[2] BLUE PILL"
    if type == 'boot':
        # Uses static effect
        if duration == 'shorter':
            os.system(CLEAR)
            printer_bold(text_console[0])
            print("\n")
            printer_bold(text_console[1])
            print(text_console[2])
            print(text_console[3])
            print("\n")
        # Uses motion effect
        elif duration == 'longer':
            os.system(CLEAR)
            time.sleep(SHORT_TIME)
            printer_bold(text_console[0])
            time.sleep(SHORT_TIME)
            print("\n")
            time.sleep(SHORT_TIME)
            printer_bold(text_console[1])
            time.sleep(MEDIUM_TIME)
            print(text_console[2])
            time.sleep(SHORT_TIME)
            print(text_console[3])
            time.sleep(SHORT_TIME)
            print("\n")

    # Displays game loading screen
    elif type == 'hangman':
        # Options screen 1
        # "SELECT LENGTH OF WORDS:"
        # "[1] FOUR TO SEVEN CHARACTERS"
        # "[2] MORE THAN SEVEN CHARACTERS"
        if screen == 1:
            # Uses static effect
            if duration == 'shorter':
                os.system(CLEAR)
                printer_bold(text_hangman[0])
                print(text_hangman[1])
                print(text_hangman[2])
                print("\n")
            # Uses motion effect
            elif duration == 'longer':
                os.system(CLEAR)
                time.sleep(SHORT_TIME)
                printer_bold(text_hangman[0])
                time.sleep(MEDIUM_TIME)
                print(text_hangman[1])
                time.sleep(SHORT_TIME)
                print(text_hangman[2])
                time.sleep(SHORT_TIME)
                print("\n")
        # Options screen 2
        # "NOUNS OR PROPER NOUNS? UMM, THAT'S NAMES BUT FANCIER"
        # "[1] FEELING FANCY"
        # "[2] NOT TODAY"
        elif screen == 2:
            # Uses static effect
            if duration == 'shorter':
                os.system(CLEAR)
                printer_bold(text_hangman[3])
                print(text_hangman[4])
                print(text_hangman[5])
                print("\n")
            # Uses motion effect
            elif duration == 'longer':
                os.system(CLEAR)
                time.sleep(SHORT_TIME)
                printer_bold(text_hangman[3])
                time.sleep(MEDIUM_TIME)
                print(text_hangman[4])
                time.sleep(SHORT_TIME)
                print(text_hangman[5])
                time.sleep(SHORT_TIME)
                print("\n")
        # Options screen 3
        # "FANCY ANOTHER SET OF ROUNDS?"
        # "[Y] I'M ALL LOOSEN UP, LET'S GO"
        # "[n] ENOUGH IS ENOUGH"
        elif screen == 3:
            # Uses static effect
            if duration == 'shorter':
                os.system(CLEAR)
                printer_bold(text_hangman[6])
                print(text_hangman[7])
                print(text_hangman[8])
                print("\n")
            # Uses motion effect
            if duration == 'longer':
                os.system(CLEAR)
                time.sleep(SHORT_TIME)
                printer_bold(text_hangman[6])
                time.sleep(MEDIUM_TIME)
                print(text_hangman[7])
                time.sleep(SHORT_TIME)
                print(text_hangman[8])
                time.sleep(SHORT_TIME)
                print("\n")
                

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