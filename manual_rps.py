import random


def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice


def get_user_choice():
    user_input = input('rock, paper, scissors? ')
    return user_input


def get_winner(computer_choice, user_choice):
    comp = computer_choice.title()
    user = user_choice.title()
    if comp == 'Rock':
        if user == 'paper':
            print('You won!')
        elif user == 'scissors':
            print('You lost')
        else:
            print('It is a tie!')
    elif comp == 'Paper':
        if user == 'rock':
            print('You lost')
        elif user == 'scissors':
            print('You won!')
        else:
            print('It is a tie!')
    elif comp == 'Scissors':
        if user == 'rock':
            print('You won!')
        elif user == 'paper':
            print('You lost')
        else:
            print('It is a tie!')


get_winner(get_computer_choice(), get_user_choice())
