# Computer Vision Rock-Paper-Scissors

## Overview
This project is a Rock-Paper-Scissors game that utilizes computer vision and machine learning to predict the player's hand gestures through a webcam. It allows the player to engage in the classic game of Rock-Paper-Scissors against the computer. The predictions are made using a Keras model trained on images of different hand gestures corresponding to rock, paper, and scissors.

### Screenshots of game

<p align="center">
  <img alt="start_game" src="assets/start_game.png?raw=true" width="47%">
&nbsp;
  <img alt="end_game" src="assets/end_game.jpg?raw=true" width="47.5%">
</p>

## Features
- Real-time hand gesture recognition
- Live countdown for each round
- Score tracking and display
- Best of five gameplay
- User-friendly interface with live feedback

## Setup
1. Clone the repository to your local machine.
2. Install the required dependencies by running:

    ```
    pip install -r requirements.txt
    ```
3. Run the script to start the game:

    ```
    python camera_rps.py
    ```
4. The input based terminal version of the game can also be run with:

    ```
    python manual_rps.py
    ```

## Usage
- Sit in front of your webcam in a well-lit area, ideally with a plain background.
- Start the game script, you will see a countdown timer on the screen.
- Make your gesture (rock, paper, or scissors) in front of the webcam within the given time like the images below.
- The computer's choice will be randomly selected, and the winner of the round will be displayed on the screen.
- The first to win three rounds wins the game.
- The live model prediction can be seen in the terminal.
- To quit the game, press 'Q' or 'q'.

## Model Training
The machine learning model is a convolutional neural network trained on a dataset of hand gesture images generated via [Teachable-Machine](https://teachablemachine.withgoogle.com/). The model is named `keras_model.h5` in this repository which relies on `labels.txt`.

If you wish to train your own model for this project, you would need to collect images of the hand gestures, label them accordingly, and train the model using Keras and TensorFlow on [Teachable-Machine](https://teachablemachine.withgoogle.com/).

## Dependencies
Please refer to `requirements.txt` for a list of dependencies.