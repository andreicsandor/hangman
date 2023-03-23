# Hangman
#### Video Demo: https://youtu.be/Rzdr12dDG68

## Description
My final project for CS50's Introduction to Programming with Python. This is a tiny Hangman game, which lets you guess words that are scraped using an API. The game stores your results so that you can keep track of your guesses, won and lost rounds.


## Contents
- **project.py** contains the ```main``` function and the other functions necessary for the game.
- **extras.py** contains in-game messages and drawings for easier editing.
- **journal.csv** stores the user’s name, guessed word, date, time and result for each round.
- **requirements.txt** lists all ```pip```-installable libraries.
- **test_project.py** contains test functions.


## Libraries
- ```csv``` for editing the .csv file and appending new lines 
- ```datetime``` for getting the current date and time
- ```os``` for clearing the terminal window
- ```pytest``` used for testing functions
- ```random``` to make random selections for list items
- ```requests``` used for scraping data containing words
- ```time``` for delaying displayed messages in the terminal


## Mechanics
- Boot up the game console via:
    ```
    python project.py
    ```
- Type your name when prompted and keep in mind to use 4-10 alphanumeric characters. If wrong input is provided, the program will re-prompt the user to enter the name again.
- The user is met with the start-up screen, where a greeting message is displayed and user-input is requested to continue to the Hangman game.
- The Hangman game menu loads, where the user can personalise the game experience by picking a word length preference and set the types of nouns that will be fetched. 
- Then, a loading screen is displayed while the program fecthes the list of words.
- After the **PRESS ENTER TO START** prompt, the game area is loaded and the word to be guessed is shown as a series of dashes at the bottom of the screen. 
- The end-goal is to guess the hidden word before the player runs out of lives. For each round, the player has 7 attempts to guess the word and each wrong input decreases the hearts number. The round is complete when the player guesses all letters or there are no more attempts left.
- The UI shows the hangman figurine and the graphics are updated to match the current number of lives, while letters are also uncovered with each correct guess.
- At the end of each round, the game stores the current round's result in a **.csv** file alongside the user's name, guessed word, date and time.
- After the default set of 3 rounds, the player can choose to play again or exit the game.
