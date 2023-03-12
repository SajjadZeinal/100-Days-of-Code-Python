# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:55:18 2022

@author: Sajjad
"""
import sys
sys.path.insert(1, "D:/100 Days of Code-Python/7/")
import random
import hangman_art , hangman_words

print(hangman_art.logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
print(f"The solution is: {chosen_word}")
display=[]
for i in range(len(chosen_word)):
    display.append("_ ")

end_of_game= False
Lives = 6


while not end_of_game: 
    guess=input("Guess a letter:\n").lower()
    i=0
    save_Live = 0
    if guess in ''.join(display):
       print(f"You have already gussed this letter.\n" + ''.join(display))
       continue
    for char in chosen_word:
        if char == guess:
            display[i] = char
            save_Live = 1
        i +=1
    print(''.join(display))
    if save_Live == 0:
        Lives -= 1
        print(stages[Lives])

    if Lives == 0:
        end_of_game = True
        print("You lost.")
    if ''.join(display) == chosen_word:
        print("You won.")





#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
