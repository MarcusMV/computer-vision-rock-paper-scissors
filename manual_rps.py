import random


def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice


def get_user_choice():
    user_input = input('Rock, Paper, Scissors? ')
    return user_input


def get_winner(computer_choice, user_choice):
    comp = computer_choice.title()
    user = user_choice.title()
    if comp == 'Rock':
        if user == 'Paper':
            print('You won!')
        elif user == 'Scissors':
            print('You lost')
        else:
            print('It is a tie!')
    elif comp == 'Paper':
        if user == 'Rock':
            print('You lost')
        elif user == 'Scissors':
            print('You won!')
        else:
            print('It is a tie!')
    elif comp == 'Scissors':
        if user == 'Rock':
            print('You won!')
        elif user == 'Paper':
            print('You lost')
        else:
            print('It is a tie!')


def play():
    get_winner(get_computer_choice(), get_user_choice())
    return

play()
