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
---------------------------------------------------
Would Like To Play Some Rock-Paper-Scissors? (Y/N)
---------------------------------------------------
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
        print("Computer Played ->")
        
        if computer_play == 'rock' {
            print(rock_gesture)
            computer = "rock"
            }
        else if computer_play == 'paper' {
            print(paper_gesture)
            computer = "paper"
            }
        else if computer_play == 'scissors' {
            print(scissors_gesture)
            computer = "scissors"
            }
        else
            print("Something went wrong? Please input a valid response!")
        
        
        switch(gesture){
            case "rock":
                print("You Played ->")
                print(rock_gesture)
                
                if computer == "scissors" {
                    print("You Win!")
                 }
                else if computer == "paper"{
                    print("You Lose!")
                 }
                else
                    print("We Tied!")
             
            case "paper":
                print("You Played ->")
                print(paper_gesture)
                
                if computer == "rock" {
                    print("You Win!")
                 }
                else if computer == "scissors"{
                    print("You Lose!")
                 }
                else
                    print("We Tied!")
            
            case "scissors":
                print("You Played ->")
                print(scissors_gesture)
                
                if computer == "paper" {
                    print("You Win!")
                 }
                else if computer == "rock"{
                    print("You Lose!")
                 }
                else
                    print("We Tied!")
         
         }
