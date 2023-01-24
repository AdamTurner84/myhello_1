#Creating a rock, paper, python game with random computer answers.

import random

computer_choice = random.choice(['rock','paper','python'])
user_choice = input('Choose rock, paper, or python: \n')

if computer_choice == user_choice:
    print('Tie, no winners here!')
elif user_choice == 'rock' and computer_choice == 'python':
    print('You won and crushed that crazy snake!!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You won, rocks dont take to no shade!!')
elif user_choice == 'python' and computer_choice == 'paper':
    print('You won, why does a snake beat paper I dont know. But you Won!!')
else:
    print('Loser! The computer beat you!')
    