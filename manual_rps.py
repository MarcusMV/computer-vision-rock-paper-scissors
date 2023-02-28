import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    options = ['rock', 'paper', 'scissors']
    user_input = input('rock, paper, scissors? ')
    if user_input in options:
        return user_input
    else:
        print('Must be rock, paper, or scissors')
        