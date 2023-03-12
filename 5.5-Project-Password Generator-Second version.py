# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:13:53 2022

@author: Sajjad
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password=[]
letter_number=len(letters)
symbol_number=len(symbols)
number_number=len(numbers)

for letter in range(1,nr_letters+1):
    password.append(random.choice(letters))
for symbol in range(1,nr_symbols+1):
    password.append(random.choice(symbols))
for number in range(1,nr_numbers+1):
    password.append(random.choice(numbers))

random.shuffle(password)
print(f"Final Password is:\n{''.join(password)}")