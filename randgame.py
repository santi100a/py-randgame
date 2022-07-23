from sys import exit
from santitools.colors import colorize
from santitools.math import random
from santitools import clear

MAX, guess, answer, player_name, play_again = 30, 0, 0, '', True
try:
    clear()
    print(colorize("Welcome to the number guessing game!", "blue"))
    player_name = input("What is your name? ")
    answer = random(MAX)
    while True:
        _guess = input(f'What\'s your guess (between 0 and {MAX})? ')
        if _guess == 'exit': break
        guess = int(_guess)
        if guess > MAX:
            clear()
            print(colorize(f"You can't guess a number higher than {MAX}!", "magenta"))
            continue
        elif guess < 0:
            clear()
            print(colorize("You can't guess a number lower than 0!", "cyan"))
            continue
        elif guess == answer:
            clear()
            print(colorize(f"Yay! {player_name}, you guessed it! ", "green"))
            def validate(inp):
                if inp == "y":
                    return True
                elif inp == "n":
                    return False
                else:
                    return True
            play_again = validate(input(f"Would you like to play again? ({colorize('y', 'green')}/{colorize('n', 'red')}) ").strip().lower()[0])
            if not play_again: break
            if play_again:
                answer = random(MAX)
                continue
        elif guess != answer:
            clear()
            print(colorize(f"Sorry {player_name}, you guessed it wrong!", "red"))
            continue
    exit(0)
except KeyboardInterrupt:
    exit(0)
except Exception as e:
    print(e)
    exit(1)