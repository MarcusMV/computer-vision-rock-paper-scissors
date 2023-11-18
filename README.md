# Computer Vision RPS
## Milestone 1 & 2
* Create an image project model from Teachable-Machine with four different classes: Rock, Paper, Scissors, Nothing. Each class is trained with images of yourself showing each option to the camera. The "Nothing" class represents the lack of option in the image. The more images trained with, the more accurate the model.
* Download the model from Tensorflow tab in Teachable-Machine: keras_model.h5, labels.txt. The files contain the structure and the parameters of a deep learning model.

## Milestone 3
* Created conda virtual environment and installed dependencies opencv-python, tensorflow and ipykernel.
* Checked the model worked as expected by running the RPS-Template.py file

## Milestone 4
* Stored the user's and computer's choices, input function to get user's choice and import random module to select random choice for computer
* Logic completed to get winner given user and computer choices
* Prints output to screen displaying if user won or lost against computer
* play() function encapsulates logic (get_computer_choice, get_user_choice, get_winner) and simulates game

## Milestone 5
* Game repeats until either computer or user wins three rounds in best of 5.
* On-screen text will show computer choice, user choice, countdown until user choice is predicted and winner.
* Made code much more readable by creating a class instead of creating multiple functions.
* Created RockPaperScissors class containing methods get_computer_choice, get_user_choice, get_winner and play_game
* Investigation into time drifting should be considered in future and details between blocking and non-blocking methods (time, datetime, threading, sched modules) -- i.e can't use the sleep function because it will stop the script, and during that time, the camera will not be able to capture the input.

## Screenshots of game

![Start Game](assets/start_game.png?raw=true "Start Game Img")
![End Game](assets/end_game.jpg?raw=true "End Game Img")