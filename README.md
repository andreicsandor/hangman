# Hangman
#### Video Demo: https://youtu.be/Rzdr12dDG68

## Description
My final project for CS50's Introduction to Programming with Python. This is a tiny Hangman game, which let's you guess words that are scraped using an API. The game stores your results so that you can keep track of your guesses, won and lost rounds.


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
