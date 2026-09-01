'''
starting the format of the rock, paper, scissors game.
ASCII drawing curtesy of (github: wynand1004)
'''

import random

rock_gesture = ("""
    _______
---l   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")

paper_gesture = ("""
    _______
---l    ____)____
           ______)
          _______)
         _______)
---.__________)

"""")

scissors_gesture = (""""
   _______
---l   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")

'''
using ascii drawing for the hand gestures and plays

'''

greeting() = input("""
----------------------------------------------
Would Like To Play Some Tic-Tac-Toe? (Y/N)
----------------------------------------------
""")

Score = 0
Turn = 0
# choose if turn based or player based ?

while (continue_game != N || continue_game != n){
        
        gesture = input("Play your hand! (rock, paper, scissors) ")
        gesture_list = ['rock', 'paper', 'scissors']
        computer_play = random.choice(gesture_list)
        
        switch (gesture){
            case rock:
                if (computer_play == rock){
                print("----------------------------------------------\nTry again!")
                # play turn again
                }
                else (computer_play == scissors) {
                print("----------------------------------------------\nYou win!")
                Score++
                print("Score is ", Score, "Hmm... Best two out of three?")
            case scissors:
                if (computer_play == rock){
                print("----------------------------------------------\nTry again!")
                # play turn again
                }
                else (computer_play == scissors) {
                print("----------------------------------------------\nYou win!")
                Score++
                print("Score is ", Score, "Hmm... Best two out of three?")
            case paper:
                if (computer_play == rock){
                print("----------------------------------------------\nTry again!")
                # play turn again
                }
                else (computer_play == scissors) {
                print("----------------------------------------------\nYou win!")
                Score++
                print("Score is ", Score, "Hmm... Best two out of three?")
            
                
                 }
         }
         }
