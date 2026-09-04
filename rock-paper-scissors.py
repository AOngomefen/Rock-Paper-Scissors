'''
Rock, Paper, Scissors game.
ASCII drawing courtesy of (github: wynand1004)
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
""")

scissors_gesture = ("""
   _______
---l   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

gestures = {
    "rock": rock_gesture,
    "paper": paper_gesture,
    "scissors": scissors_gesture,
}

gesture_list = ["rock", "paper", "scissors"]

# What beats what: key beats value
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

player_score = 0
computer_score = 0
turn = 0

continue_game = input("Would You like to Play? (Y/N) ").strip().upper()
while continue_game not in ("Y", "N"):
    continue_game = input("Input Invalid! Try Again (Y/N) ").strip().upper()

while continue_game == "Y":
    turn += 1

    # validate player input
    gesture = input("Play your hand! (rock, paper, scissors) ").strip().lower()
    while gesture not in gesture_list:
        gesture = input("Invalid choice. Play rock, paper, or scissors: ").strip().lower()

    computer = random.choice(gesture_list)

    print("Computer Played ->")
    print(gestures[computer])

    print("You Played ->")
    print(gestures[gesture])

    if gesture == computer:
        print("We Tied!")
    elif beats[gesture] == computer:
        print("You Win!")
        player_score += 1
    else:
        print("You Lose!")
        computer_score += 1

    print("Player Score:", player_score)
    print("Computer Score:", computer_score)

    continue_game = input("Play again? (Y/N) ").strip().upper()
    while continue_game not in ("Y", "N"):
        continue_game = input("Input Invalid! Try Again (Y/N) ").strip().upper()

print(f"\nThanks for playing! Final score - You: {player_score}, Computer: {computer_score}")
