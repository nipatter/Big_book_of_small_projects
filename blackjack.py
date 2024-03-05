'''
A game of blackjack
By Nigel Patterson

This program plays a 2-player game of blackjack. The CPU is the dealer.
'''

def rules():
    '''Just gives the rules of the game'''
    print('''
    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
    ''')

import random, sys

def create_deck():
    '''Create a full deck of 52 cards
    This makes it easier to play with a smaller deck
    '''
    
    # Set up the constants:
    HEARTS   = chr(9829) # Character 9829 is '♥'.
    DIAMONDS = chr(9830) # Character 9830 is '♦'.
    SPADES   = chr(9824) # Character 9824 is '♠'.
    CLUBS    = chr(9827) # Character 9827 is '♣'.
    BACKSIDE = '#'
    
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] #replace aces after fixing bugs
    suits = [HEARTS, DIAMONDS, SPADES, CLUBS]

    return [v+s for v in values for s in suits]


def render_card(v: str, s: str) -> None: # value, suit
    '''Draw how the cards look on the screen'''

    card_art = f'''
     ___
    |{v}  |
    | {s} |
    |__{v}|
    '''
    print(card_art, end="  ") # FIXME figure out how to suppress the newline


def deal_a_card(deck, person):
    '''Deal a card to the players'''
    return person.append(deck.pop(0))


def initial_deal(deck: list) -> list:
    '''Start the game by dealing out the cards'''
   
    random.shuffle(deck)
    dealers_hand = []
    players_hand = []

    for i in range(2):
        deal_a_card(deck, players_hand)
        deal_a_card(deck, dealers_hand)

    # Show the second of the dealer's cards
    dealers_total = get_hand_value(dealers_hand)

    print(f"Dealer's hand: {dealers_total}") # TODO: hide this value in the finished game
    hidden_card = list(dealers_hand[0])
    render_card(hidden_card[0], hidden_card[1]) # change this to hide the card later.

    shown_card = list(dealers_hand[1])
    render_card(shown_card[0], shown_card[1])
    print("\n")
    print("----------------------------------------")


    # Show player's cards
    players_total = get_hand_value(players_hand)

    print(f"Player's hand: {players_total}")
    for card in players_hand:
        card = list(card)
        render_card(card[0], card[1])
    
    return [dealers_hand, players_hand]


def get_card_value_without_aces(card):
    '''Get the value of a single card'''

    num_value = 0
    card_value = list(card)
    print(card_value) # TODO: remove when finished debugging

    if card_value[0] == 'K' or 'Q' or 'J':
        num_value = 10
    elif card_value[0] == 'A':
        num_value = 0 # don't do anything
    else:
        num_value = int(card_value[0])

    return num_value


def get_hand_value(hand):
    '''Calculate the total value of a hand'''

    print(hand) #TODO remove when finished debugging
    hand_total = 0
    
    for card in hand:
        list(card)
        if card[0] != 'A':
            hand_total += get_card_value_without_aces(card)
        if card[0] == 'A' and hand_total+11 <= 21:
            hand_total += 11
        elif card[0] == 'A' and hand_total+11 > 21:
            hand_total += 1

    return hand_total


def one_round():
    '''Play a round of blackjack'''



    # ask the player if they want to double down?


def place_bet(current_cash: int) -> int:
    '''Ask the player to place their bet'''
    try:   
        bet = int(input("How much do you want to bet? "))
    except ValueError:
        print("Error: You need to provide an integer value")
        place_bet(current_cash)

    if bet > current_cash:
        print("You can't afford this bet")
        place_bet(current_cash)
    
    return bet


def double_down():
    '''Ask the player if they want to double their bet'''
    double_ans = input("Double down? y/n: ")
    if double_ans == 'y':
        return True
    elif double_ans == 'n':
        return False
    else:
        print('Invalid input. try again')
        double_down()


def who_won():
    '''Determine the winner of the game'''



def main():
    '''Main gameplay program'''

    try:
        cash = int(input("how much cash did you bring today? "))
    except ValueError:
        print("Error: You need to provide an integer value")
        main()

    deck = create_deck()
    place_bet(cash) # enusre this cash value is updated based on wins/losses
    initial_deal(deck)
    #one_round(play)

rules()
main()