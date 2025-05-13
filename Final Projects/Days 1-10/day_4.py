# Rock, paper, scissors
import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps = [rock, paper, scissors]
computers_choice = random.choice(rps)
players_choice = int(input(f"What would you like to play? Type 0 for rock, 1 for paper, and 2 for scissors.\n"))
print(f"Your choice: {rps[players_choice]}")
print(f"Computer's choice: {computers_choice}")
if players_choice == 0:
    if computers_choice == scissors:
        print("You won!")
    elif computers_choice == paper:
        print("You lose!")
    else:
        print("It's a tie!")
if players_choice == 2:
    if computers_choice == paper:
        print("You won!")
    elif computers_choice == rock:
        print("You lose!")
    else:
        print("It's a tie!")
if players_choice == 1:
    if computers_choice == rock:
        print("You won!")
    elif computers_choice == scissors:
        print("You lose!")
    else:
        print("It's a tie!")
