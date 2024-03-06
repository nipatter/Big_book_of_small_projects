"""
Cho Han is a dice game. Two six-sided dice are rolled in a cup and
the player must guess if the sum is even or odd.
"""

from random import randint

class Wallet:
    """Keeps track of how much money the player has."""
    def __init__(self):
        self.coins = 0

    def update_money(self, coins=0):
        '''Updates the amount of money in the wallet'''
        self.coins += coins
        return self.coins
    
    def show_money(self):
        '''Shows the current amount of money in the wallet'''
        return self.coins


def roll_dice(num_dice: int, num_sides: int,) -> int:
    """Roll x number of d-y sided dice"""
    dice_total = 0
    i = 0
    for i in range(num_dice):
        dice_total += randint(1, num_sides)
    return dice_total


def check_odd_even(number: int) -> str:
    """Check if a number is odd or even"""
    if number % 2 == 0:
        return "cho"
    if number % 2 == 1:
        return "han"
    #else:
    #    raise Exception("Not a valid integer.")


def get_guess() -> str:
    """Ask the player for their guess"""
    print("Is the sum of the hidden dice even (cho) or odd (han)?")
    guess = input("Cho/Han? > ")
    return guess.lower()


def get_bet(current_money: int) -> int:
    """Ask the player how much money they want to bet."""
    print('How much do you want to bet? (or (Q)UIT)')
    bet = input("bet amount > ")
    
    if bet in ("QUIT", "quit", "Q", "q"):
        return False
        
    try:
        bet = int(bet)
    except ValueError:
        print("Invalid amount given")
        return False

    if bet > current_money:
        print(f"Insufficient funds, the most you can bet is {current_money}")
        return get_bet(current_money)
    elif bet == 0:
        print("You gotta pay to play. Minimum bet is $1.")
        return get_bet(current_money)
    elif bet < 0:
        print("This is just a reverse bet.")
        return bet
    else:
        return bet


def print_rules():
    """Print the rules of the game"""
    print("""
    In this traditional Japanese dice game, two dice are rolled in a bamboo
    cup by the dealer sitting on the floor. The player must guess if the
    dice total to an even (cho) or odd (han) number.    
    """)


def main(num_dice, die_sides):
    """Main game loop"""
    print_rules()

    print(f"This game will be played with {num_dice} {die_sides}-sided dice.")

    wallet = Wallet()
    wallet.update_money(5000)
    print(f"You start with ${wallet.show_money()}")

    game_session = True

    while game_session:
        round_bet = get_bet(wallet.show_money())

        if round_bet is False:
            break

        total = roll_dice(num_dice, die_sides)
        
        correct_answer = check_odd_even(total)
        player_answer = get_guess()

        print(total)
        if correct_answer == player_answer:
            wallet.update_money(round_bet)
            print(f"You win +${round_bet}. You now have ${wallet.show_money()}")
        elif correct_answer != player_answer:
            wallet.update_money(-round_bet)
            print(f"You lose -${round_bet}. You now have ${wallet.show_money()}")


main(12, 20)