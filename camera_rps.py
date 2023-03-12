import random
import time
from dataclasses import dataclass, field
#from threading import timer
import cv2
from keras.models import load_model
import numpy as np

@dataclass
class RockPaperScissors:
    options: list[str] = field(default_factory=lambda: ['rock', 'paper', 'scissors', 'none'])
    maximum_time: int = 5

    def get_computer_choice(self):
        computer_choice = random.choice(self.options[:-1])
        return computer_choice
    
    def get_user_choice(self, prediction):
        return self.options[prediction]

    def get_winner(self, user_choice, computer_choice):
        comp = computer_choice.title()
        user = user_choice.title()
        winner = None

        if comp == 'Rock':
            if user == 'Paper':
                winner = 'user'
            elif user == 'Scissors':
                winner = 'computer'
            else:
                winner = 'tie'
        elif comp == 'Paper':
            if user == 'Rock':
                winner = 'computer'
            elif user == 'Scissors':
                winner = 'user'
            else:
                winner = 'tie'
        elif comp == 'Scissors':
            if user == 'Rock':
                winner = 'user'
            elif user == 'Paper':
                winner = 'computer'
            else:
                winner = 'tie'
        return winner

    def play_game(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        computer_wins = 0
        user_wins = 0

        start_time = time.time()

        while True:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) /
                                127.0) - 1  # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            #start = time.time()

            curr_time = time.time()
            remaining_time = int(self.maximum_time - (curr_time - start_time))
            countdown_text = f"Predict In: {remaining_time}"
            # pred = 'test'
            cv2.putText(frame, countdown_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            # cv2.putText(frame, pred, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            cv2.imshow('frame', frame)
            # Press q to close the window
            #print('pred:', prediction[0])

            # curr_time = time.time()
            if (curr_time - start_time) >= self.maximum_time:
                # print(prediction)
                # pred_list = prediction[0][0].split(' ')
            #print('pred:', prediction[0])
            #print('pred:', prediction[0])
                # cv2.putText(frame, 'test', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                pred_arr = prediction[0]
                max_index = np.where(pred_arr == np.max(pred_arr))
                
                user_choice = self.get_user_choice(max_index[0][0])
                cv2.putText(frame, f"You chose: {user_choice}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow('frame', frame)
                computer_choice = self.get_computer_choice()
                if user_choice != 'none':
                    winner = self.get_winner(user_choice, computer_choice)

                    print('USER chose:', user_choice)
                    print('COMPUTER chose:', computer_choice)

                # computer_wins += 1 if winner == 'computer' else user_wins + 1
                if winner == 'computer':
                    computer_wins += 1
                    print(winner.upper(), 'wins this round.')
                elif winner == 'user':
                    user_wins += 1
                    print(winner.upper(), 'wins this round.')
                else:
                    print('It\'s a tie.')
            
                if computer_wins == 3:
                    print('\nCOMPUTER wins the best of 5!')
                    break
                elif user_wins == 3:
                    print('\nUSER wins the best of 5!')
                    break

                start_time = curr_time

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        #print('prediction: ', prediction)
        return
    
start = RockPaperScissors()
start.play_game()

