import random

class RockPaperScissors:
    def __init__(self) -> None:
        self.options = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.options)

    def get_user_choice(self):
        user_input = input('Rock, Paper, Scissors? ').lower()

        while user_input not in self.options:
            user_input = input('Invalid choice. Please choose Rock, Paper, or Scissors. ').lower()

        return user_input

    def get_winner(self, computer_choice, user_choice):
        print(f'\nComputer picked {computer_choice.title()}')
        print(f'You picked {user_choice.title()}')

        if computer_choice == user_choice:
            return '\nIt is a tie!'
        if (computer_choice == 'rock' and user_choice == 'scissors') or \
           (computer_choice == 'paper' and user_choice == 'rock') or \
           (computer_choice == 'scissors' and user_choice == 'paper'):
            return '\nComputer wins!'
        else:
            return '\nYou win!'
        
    def play(self):
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        result = self.get_winner(computer_choice, user_choice)

        print(result)    

# Create an instance of the game and play
game = RockPaperScissors()
game.play()
