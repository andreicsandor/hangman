# Messages
messages_loading = ["TYING UP ROPE KNOT...", "UNCOILING A BRAND NEW ROPE...", "HANG ON, TIDYING UP HERE..."]
messages_losing = ["~~ NEXT TIME... MAYBE. ~~", "~~ TRY HARDER. ~~", "~~ SO CLOSE... BUT SO FAR AWAY. ~~", "~~ WHAT A BUMMER! ~~"]
messages_winning = ["~~ WAY TO GO! ~~", "~~ BAZINGA! ~~", "~~ WELL PLAYED! ~~", "~~ GOOD ONE! ~~"]
text_console = [
        "WELCOME TO CS50 🕹️  STATION", # 0
        "WANNA PLAY A GAME?", # 1
        "[1]   RED PILL", # 2
        "[2]   BLUE PILL" # 3
    ]
text_hangman = [
        "SELECT LENGTH OF WORDS:", # 0
        "[1]   FOUR TO SEVEN CHARACTERS", # 1
        "[2]   MORE THAN SEVEN CHARACTERS", # 2
        "NOUNS OR PROPER NOUNS? UMM, THAT'S NAMES BUT FANCIER", # 3
        "[1]   FEELING FANCY", # 4
        "[2]   NOT TODAY", # 5
        "THAT'S IT! FANCY ANOTHER SET OF ROUNDS?", # 6
        "[Y]   SHOOT YOUR NEXT WORD", # 7
        "[n]   ENOUGH IS ENOUGH", # 8
    ]


# Drawings
divider = "~" * 15
hangman_splash = ["THIS IS HANG_AN", "", divider, " |", " |     / \\", " |     /|\\", " |     ( )", " |      |", " ________"]
hangman_empty = ["", "", divider, " |", " |         ", " |         ", " |        ", " |       ", " ________", "", ""]
hangman_progress = {
        0: """ ________
 |      |
 |     ( )
 |     /|\\
 |     / \\
 |
~~~~~~~~~~~~~~~
""",
        1: """ ________
 |      |
 |     ( )
 |     /|\\
 |     /
 |
~~~~~~~~~~~~~~~
""",
        2: """ ________
 |      |
 |     ( )
 |     /|\\
 |
 |
~~~~~~~~~~~~~~~
""",
        3: """ _________
 |      |
 |     ( )
 |     /|
 |
 |
~~~~~~~~~~~~~~~
""",
        4: """ ________
 |      |
 |     ( )
 |      |
 |
 |
~~~~~~~~~~~~~~~
""",
        5: """ ________
 |      |
 |     ( )
 |
 |
 |
~~~~~~~~~~~~~~~
""",
        6: """ ________
 |      |
 |
 |
 |
 |
~~~~~~~~~~~~~~~
""",
        7: """ ________
 |
 |
 |
 |
 |
~~~~~~~~~~~~~~~
"""
    }
