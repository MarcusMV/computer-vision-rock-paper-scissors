import random


choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    computer_choice = random(choices)
    return computer_choice

def get_user_choice():
    user_input = input('rock, paper, scissors? ')
    if user_input in choices:
        return user_input
    else:
        print('Must be rock, paper, or scissors')
        