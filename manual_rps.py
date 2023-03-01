import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice


def get_user_choice():
    user_input = input('rock, paper, scissors? ')
    return user_input


def get_winner(computer_choice, user_choice):
    comp = computer_choice.lower()
    user = user_choice.lower()
    if comp == 'rock':
        if user == 'paper':
            print('Paper beats rock, user wins')
        elif user == 'scissors':
            print('Rock beats scissors, computer wins')
        else:
            print('It\'s a draw')
    elif comp == 'paper':
        if user == 'rock':
            print('Paper beats rock, computer wins')
        elif user == 'scissors':
            print('Scissors beats paper, user wins')
        else:
            print('It\'s a draw')
    elif comp == 'scissors':
        if user == 'rock':
            print('Rock beats scissors, user wins')
        elif user == 'paper':
            print('Scissors beats paper, computer wins')
        else:
            print('It\'s a draw')


get_winner(get_computer_choice(), get_user_choice())
