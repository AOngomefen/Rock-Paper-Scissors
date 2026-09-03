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
turn = 0

continue_game = input("Would You like to Play? (Y/N)")
while (continue_game != 'N' || continue_game != 'Y' ){
    continue_game = input("Input Invalid! Try Again")
    }


# choose if turn based or player based ?

while (continue_game != 'N' || continue_game != 'n'){
        
        gesture = input("Play your hand! (rock, paper, scissors) ")
        #validate input
        gesture_list = ['rock', 'paper', 'scissors']
        computer_play = random.choice(gesture_list)
        
        switch(gesture){
            case rock:
                print("You Played ->")
                print(rock_gesture)
                print("Computer Played ->")
                print(
                
                if computer_play == gesture {
                
                 }
                
                 }
        
        
         
         }
