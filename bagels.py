'''
Bagels, a deductive logic game.
By Nigel Patterson
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digits are correct.
'''

from random import randint
import sys

def check_guess(guess: int, secret: int) -> list:
    '''Checks for matching numbers at each digit'''

    hints = [] # FIXME: huge issue when repeated digit in guess appears in secret
    
    for ind, digit in enumerate(guess):
        if guess == secret:
            hints.append("Correct")
        elif digit == secret[ind]:
            hints.append('Fermi')
        elif digit in secret:
            hints.append('Pico')

    if not hints:
        hints.append('Bagels')

    hints.sort()
    return hints


def play_again() -> None:
    '''Ask the player if they want to have another go'''
    answer = input("Play again? y/n: ")
    if answer == "y":
        main_game(10)
    else:
        sys.exit()


def main_game(chances: int) ->  None:
    '''The main game loop'''

    secret_num = str(randint(100, 999))

    print("Guess the secret 3 digit number (100 - 999)")
    print("Here are what the hints mean: \n* Bagels: nothing right \n* Pico: right digit wrong place \n* Fermi: right digit right place\n")

    #print(secret_num) # TODO remove for final version

    for i in range(chances, -1, -1):
        if i == 0: ## this code doesn't execute because it stops before i == 0
            print("Game Over. You've run out of guesses.")
            print(f"The correct answer was {secret_num}")
            play_again()

        print(f"You have {i} guesses left")
        guess_num = input("Guess: ")

        hint_feedback = check_guess(guess_num, secret_num)
        if "Correct" in hint_feedback:
            print("You guessed the answer correctly")
            play_again()
        else:
            for hint in hint_feedback:
                print(hint, end=' ')
            print("\n")


main_game(10)
