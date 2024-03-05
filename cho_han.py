"""
Cho Han is a dice game. Two six-sided dice are rolled in a cup and
the player must guess if the sum is even or odd.
"""

from random import randint

def roll_die(d_num: int) -> int:
    """Roll a d-x sided die"""
    roll = randint(1, d_num)
    return roll


def check_odd_even(number: int) -> str:
    """Check if a number is odd or even"""
    if number//2 == 0:
        return "cho"
    if number//2 == 1:
        return "han"
    else:
        raise Exception("Not a valid integer.")


def get_guess() -> str:
    """Ask the player for their guess"""
    print("Is the sum of the hidden dice even (cho) or odd (han)?")
    guess = input("Cho/Han? > ")
    return guess.lower()


def banker(update_money: int) -> int:
    """Keeps track of how much money the player has."""
    coins = 0
    coins += update_money
    print(f"Total cash: ${coins}")


def get_bet() -> int:
    """Ask the player how much money they want to bet."""
    print('How much do you want to bet? (or QUIT)')
    bet = int(input("bet > "))
    return bet


def print_rules():
    """Print the rules of the game"""
    print("""
    In this traditional Japanese dice game, two dice are rolled in a bamboo
    cup by the dealer sitting on the floor. The player must guess if the
    dice total to an even (cho) or odd (han) number.    
    """)


def main(num_dice):
    """Main game loop"""
    print_rules()

    starting_cash = 5000
    banker(starting_cash)

    game_session = True

    while game_session:
        #round_bet = get_bet()

        # if round_bet == "QUIT":
            # game_session = False

        sum_of_dice = 0
        for i in range(num_dice):
            sum_of_dice += roll_die(6)
            i+= 1
        
        print(sum_of_dice)

        correct_answer = check_odd_even(sum_of_dice)
        player_answer = get_guess()

        if correct_answer == player_answer:
            print("win")
            # banker(round_bet*2)
        else:
            # banker(-round_bet)
            print("lose")

main(2)