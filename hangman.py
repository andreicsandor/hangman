import csv
import os
import random
import requests
import time

from datetime import datetime
from extras import hangman_splash, hangman_empty, hangman_progress, messages_winning, messages_losing, messages_loading, text_console, text_hangman
from random import choice


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


def boot_console():
    """Boots up the game console and displays games choices."""

    # Clears the terminal console
    os.system(CLEAR)
    # Awaits seconds
    time.sleep(LONG_TIME)

    printer_bold("BOOTING UP...")
    time.sleep(LONG_TIME)

    attempts = 0

    while True:

        os.system(CLEAR)
        time.sleep(MEDIUM_TIME)

        # Displays initial greeting message
        if attempts == 0:
            printer_bold("HELLO, HUMAN.")
            print("\n")
        else:
            printer_bold("HELLO, HUMAN. YET AGAIN.")
            print("\n")

        attempts += 1

        time.sleep(LONG_TIME)
        name = input("TYPE YOUR NAME... ").strip()

        if validate_name(name):
            name = name.upper()
            break
        else:
            os.system(CLEAR)
            time.sleep(MEDIUM_TIME)
            printer_bold("NAME SHOULD BE 4 TO 10 CHARACTERS LONG AND CONSIST OF ALPHANUMERIC CHARACTERS. LET'S TRY AGAIN...")
            time.sleep(LONG_TIME * 3)

    # Displays loading screen with waiting time
    # "WELCOME TO CS50 🕹️ STATION"
    # "WANNA PLAY A GAME?"
    # "[1] RED PILL"
    # "[2] BLUE PILL"
    printer("boot", "longer")

    while True:

        # Displays loading screen with NO waiting time
        printer("boot", "shorter")

        # Prompts the user to pick a game
        game = input("SELECT YOUR OPTION AND PRESS ENTER... ").strip()

        # Validates the input
        try:
            if int(game) in [1, 2]:
                # Returns the user's picked game
                return name, game
        except ValueError:
            continue


def load_hangman(name):
    """Loads the Hangman game."""

    os.system(CLEAR)
    time.sleep(LONG_TIME)

    # Prints the welcome screen
    printer_reverse(hangman_splash)

    # Awaits user input
    time.sleep(MEDIUM_TIME)
    print("\n")
    time.sleep(SHORT_TIME)
    input("PRESS ENTER TO START GAME... ")

    # Displays options screen with waiting time
    # "SELECT LENGTH OF WORDS:"
    # "[1] FOUR TO SEVEN CHARACTERS"
    # "[2] MORE THAN SEVEN CHARACTERS"
    time.sleep(MEDIUM_TIME)
    printer("hangman", "longer", 1)

    while True:

        # Displays options screen with NO waiting time
        printer("hangman", "shorter", 1)

        # Prompts the user to pick an option
        length = input("SELECT OPTION AND PRESS ENTER... ").strip()

        # Validates the input
        try:
            if int(length) in [1, 2]:
                length = int(length)
                break
        except ValueError:
            continue

    # Displays options screen with waiting time
    # "NOUNS OR PROPER NOUNS? UMM, THAT'S NAMES BUT FANCIER"
    # "[1] FEELING FANCY"
    # "[2] NOT TODAY"
    time.sleep(MEDIUM_TIME)
    printer("hangman", "longer", 2)

    while True:

        # Displays options screen with NO waiting time
        printer("hangman", "shorter", 2)

        # Prompts the user to pick an option
        uppercase = input("SELECT OPTION AND PRESS ENTER... ").strip()

        # Validates the input
        try:
            if int(uppercase) in [1, 2]:
                uppercase = int(uppercase)
                break
        except ValueError:
            continue

    # Displays loading screen
    os.system(CLEAR)
    time.sleep(SHORT_TIME)
    printer_bold("HOLD STEADY, FLIPPING THROUGH DICTIONARY PAGE")
    time.sleep(SHORT_TIME)
    print("\n")

    # Fetches the list of words
    words = fetch_words(length, uppercase)

    # Awaits user input
    input("DONE! PRESS ENTER TO PLAY... ")

    # Executes the game
    play_hangman(name, words)


def play_hangman(name, words):
    """Executes the Hangman game."""

    # Iterates through the rounds
    round = 0
    while round < ROUNDS:
        os.system(CLEAR)
        time.sleep(MEDIUM_TIME)

        # Picks the round's word
        word = words[round]

        # Sets the no. of lives per round
        lives = MAX_LIFE
        hearts = "❤️" * lives

        # Sets the no. of correct guesses needed
        target = len(word)
        points = 0
        guessed = []

        # Prepares the visual elements
        hangman_empty[10] = f"ROUND: {round+1}"
        hangman_empty[9] = f"LIVES: {hearts}"
        hangman_empty[0] = "-" * len(word)

        #################################
        # print(word) # Testing purposes
        #################################

        # Prints the empty hangman figurine
        printer_reverse(hangman_empty)

        # Stops the game when target points are achieved or all lives are lost
        while lives > 0 and points < target:
            # Awaits the user's input
            print("\n")
            guess = input("TYPE LETTER... ").upper().strip()

            # Checks whether the input has already been introduced
            if guess in guessed:
                print("\n")
                printer_bold("~~ HMM, I'VE SEEN THIS ONE BEFORE... ~~")
                time.sleep(LONG_TIME * 2)

                # Updates the hangman figurine
                # Uses static effect
                os.system(CLEAR)
                printer_bold(hangman_empty[10])
                printer_bold(hangman_empty[9])
                printer_bold(hangman_progress[lives])
                printer_bold(hangman_empty[0])
            else:
                guessed.append(guess)

                # Checks whether the word contains the user's entered letter
                indexes = find_indexes(word, guess)

                # Handles the case when the player's guess is correct
                if indexes != []:

                    for index in indexes:
                        # Replaces "-" with the guessed letter
                        # Copies the word into a list of characters
                        characters_list = list(hangman_empty[0])
                        characters_list[index] = guess
                        hangman_empty[0] = "".join(characters_list)
                        points += 1

                    # Displays congratulations message
                    print("\n")
                    printer_bold(choice(messages_winning))
                    time.sleep(LONG_TIME * 2)

                    # Updates the hangman figurine
                    # Uses static effect
                    os.system(CLEAR)
                    printer_bold(hangman_empty[10])
                    printer_bold(hangman_empty[9])
                    printer_bold(hangman_progress[lives])
                    printer_bold(hangman_empty[0])

                    # Handles the case when all letters were correctly guessed
                    if points == target:

                        # Marks the round as complete
                        round += 1

                        print("\n")
                        printer_bold("~~ YOU WON! ~~")
                        time.sleep(LONG_TIME * 3)

                        # Write result in the journal
                        save_result(name, word, "PASSED")

                # Handles the case when the player's guess is incorrect
                else:
                    # Decreases no. of lives
                    lives -= 1
                    hearts = "❤️" * lives
                    hangman_empty[9] = f"Lives: {hearts}"

                    # Displays encouragement message
                    print("\n")
                    printer_bold(choice(messages_losing))
                    time.sleep(LONG_TIME * 2)

                    # Updates the hangman figurine
                    # Uses static effect
                    os.system(CLEAR)
                    printer_bold(hangman_empty[10])
                    printer_bold(hangman_empty[9])
                    printer_bold(hangman_progress[lives])
                    printer_bold(hangman_empty[0])

                    # Handles the case when no more lives are left
                    if lives == 0:

                        # Marks the round as complete
                        round += 1

                        os.system(CLEAR)
                        printer_bold(hangman_empty[10])
                        printer_bold(hangman_empty[9])
                        printer_bold(hangman_progress[0])
                        printer_bold(word)
                        print("\n")
                        printer_bold("~~ YOU LOST! ~~")

                        time.sleep(LONG_TIME * 3)

                        # Write result in the journal
                        save_result(name, word, "FAILED")

        if round != ROUNDS:
            os.system(CLEAR)
            printer_bold(choice(messages_loading))
            time.sleep(LONG_TIME * 2)
        else:
            # "FANCY ANOTHER SET OF ROUNDS?"
            # "[Y] I'M ALL LOOSEN UP, LET'S GO"
            # "[n] ENOUGH IS ENOUGH"
            printer("hangman", "longer", 3)

            while True:

                # Displays options screen with NO waiting time
                printer("hangman", "shorter", 3)
                # Prompts the user to pick an option
                answer = input("SELECT OPTION AND PRESS ENTER... ").strip()
                # Validates the input
                try:
                    if answer.upper() == "Y":
                        round = 0
                        break
                    if answer.upper() == "N":
                        break
                except ValueError:
                    continue

    # Displays game end screen
    os.system(CLEAR)
    hangman_splash[0] = "THIS WAS HANGMAN"
    printer_reverse(hangman_splash)
    time.sleep(MEDIUM_TIME)
    print("\n")
    time.sleep(SHORT_TIME)
    print("THE END.")


def save_result(name, word, status):
    """Keeps a journal of each user's guessed word."""

    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    with open("journal.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "name", "word", "guess"])
        writer.writerow({"date": date, "name": name, "word": word, "guess": status})


def fetch_words(length, uppercase):
    """Gets the API response and validates the list of words."""

    # Sets the length criteria
    if length == 1:
        min_length = 4
        max_length = 7
    elif length == 2:
        min_length = 8
        max_length = 15
    # Sets the uppercase criteria
    if uppercase == 1:
        option_uppercase = True
    elif uppercase == 2:
        option_uppercase = False

    # API Wordnik
    url = f"https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=1&minLength={str(min_length)}&maxLength={str(max_length)}&limit={str(LIMIT)}&api_key={KEY}"

    # Gets API response
    response = requests.get(url)
    object = response.json()

    # Picks three random words from the sample
    positions = []
    words = []
    for _ in range(ROUNDS):
        condition_char = 'fail'
        while condition_char == 'fail':
            position = random.randint(0, LIMIT-1)

            # Checks whether the position was previously selected
            while True:
                if position in positions:
                    position = random.randint(0, LIMIT-1)
                else:
                    break

            # Remembers the randomly selected position
            positions.append(position)

            # Stores the word
            word = object[position]["word"]

            # Validates the word
            if "-" not in word and " " not in word and "." not in word and "'" not in word:
                condition_uppercase = 'pass'
                if option_uppercase:
                    if word[0].islower() == True:
                        condition_uppercase = 'fail'
                else:
                    if word[0].isupper() == True:
                        condition_uppercase = 'fail'
                if condition_uppercase == 'pass':
                    condition_char = 'pass'
                    words.append(word.upper())

    return words


def find_indexes(word, guess):
    """Returns a list of indexes for matched characters in the word."""
    indexes = []

    for index, character in enumerate(word):
        if character == guess:
            indexes.append(index)
    return indexes


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