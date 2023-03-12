# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:06:31 2022

@author: Sajjad
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player_choice == 0:
    print(f"You : \n {rock}")
elif player_choice == 1:
    print(f"You : \n {paper}")
else:
    print(f"You : \n {scissors}")

computer_choice=random.randint(0, 2)

if computer_choice == 0:
    print(f"Computer : \n {rock}")
elif computer_choice == 1:
    print(f"Computer : \n {paper}")
else:
    print(f"Computer : \n {scissors}")
    
if computer_choice == player_choice:
    print("Result: Draw")
elif computer_choice - player_choice == 1 or computer_choice - player_choice == -2:
    print("You are Lost.")
else:
    print("You are Winner.") 
    
