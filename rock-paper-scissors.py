'''
starting the format of the rock, paper, scissors game.

'''

rock = ("""
    _______
---l   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")

paper = ("""
    _______
---l    ____)____
           ______)
          _______)
         _______)
---.__________)

"""")

scissors = (""""
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

while (greeting == Y){
        gesture = input("Play your hand! (rock, paper, scissors) ")
        #random -> select gesture
        
        switch (gesture){
            case rock:
                if (computer_play = rock){
                print("----------------------------------------------/nscore is tied!")
         }
         }
         }
