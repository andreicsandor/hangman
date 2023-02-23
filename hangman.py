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