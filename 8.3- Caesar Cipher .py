# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:37:14 2022

@author: Sajjad
"""
import sys
sys.path.insert(1, "D:/100 Days of Code-Python/8/art")
import random
import art

print(art.logo)

def cipher (text, shift):
    if direction == "encode":
       encrypted_list=[]
       for letter in text:
           if letter not in alphabet:
              encrypted_list.append(letter)
              continue
           if alphabet.index(letter) + shift < 26:
               encrypted_list.append(alphabet[alphabet.index(letter) + shift])
           else:
               encrypted_list.append(alphabet[(alphabet.index(letter) + shift) % 26])
       print(''.join(encrypted_list))
    elif direction == "decode":
       decrypted_list=[]
       for letter in text:
           if letter not in alphabet:
              encrypted_list.append(letter)
              continue
           if alphabet.index(letter) - shift >= 0:
               decrypted_list.append(alphabet[alphabet.index(letter) - shift])
           else:
               decrypted_list.append(alphabet[(alphabet.index(letter) - shift) % 26])
       print(''.join(decrypted_list)) 


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


run = True

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(text, shift)
    run_again = input("Do you want to run again?[Yes/No]\n")
    if run_again == "No":
        run = False
    

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

        