'''
The Birthday Paradox, AKA the Birthday Problem
By Nigel Patterson

A Monte Carlo simulation.
For a given group size, what is the probability of
two or more people having a matching birthday?
'''

from random import randint

def generate_birthdays() -> int:
    '''Generate a birthday, with consideration for leap years every 4 years'''
    day = randint(1, 366) # TODO: doesn't this change the probability of other birthdays?
    if day == 60: # 31+29 = 60, leap days are the 60th day in the calendar
        reroll = randint(1,4) # leap years happen every 4 years
        if reroll != 4: # pseudo way of making 60 1/4 as common as other numbers
            generate_birthdays() # is this recursion?? no becuase it doesn't collapse down to a value
        else:
            return day
    else:
        return day


def one_simulation(num_people: int) -> bool:
    '''Data from one simulation'''
    birthday_list = []
    for i in range(num_people):
        birthday_list.append(generate_birthdays())

    # print(f"Here are {num_people} people's birthdays: {birthday_list}")
    # this is for debugging only. unless you want to see 10000 birthday lists printed

    # check for any matching pairs
    if len(birthday_list) == len(set(birthday_list)):
        return False # no matching birthdays
    else:
        return True # some people had matching birthdays


def main() -> None:
    '''main birthday game'''
    try:
        group_size = int(input("How many people in the group? (100 max) "))
    except ValueError:
        print("Error: You need to give an integer value")
        main()
    if group_size > 100:
        print("Error: Too many darn people!")
        main()
    
    try:
        num_of_sims = int(input("How many simulations should I run? "))
    except ValueError:
        print("Error: You need to give an integer value")
        main()

    match_counter = 0

    for i in range(num_of_sims):
        if i % 10000 == 0:
            print(f"{i} simulations run...")
        if one_simulation(group_size) is True:
            match_counter += 1

    # matching birthday probability
    prob = match_counter/num_of_sims * 100

    print(f'''Out of {num_of_sims} simulations of {group_size} people, there was a
    matching birthday in that group {match_counter} times. This means that {group_size} people 
    have a {prob:.5f} % chance of having a matching birthday in their group.''')


main()
