# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:41:12 2022

@author: Sajjad
"""
import sys
sys.path.insert(1, "D:/100 Days of Code-Python/9/art")
import art

print(art.logo)
from os import system
bidders = {}


def add_bidder(name,price):
    bidders[name]= f"${price}"
    

countinue_bidding = "Yes"

while countinue_bidding == "Yes":
    print("What is your name?")
    name=input()
    price=int(input("your Bid:$ "))
    add_bidder(name, price)
    decision = input("Are there any other bidders? Type 'yes' or 'no'.")
    if decision == "No":
       countinue_bidding = "No"
    elif decision == "Yes":
       print(chr(27) + "[H" + chr(27) + "[J")
i=0
for key in bidders:
    if i==0:
        winner_name = key
        winner_price = bidders[winner_name]
        i += 1 
    else:
        if bidders[key] > winner_price:
            winner_name = key
            winner_price = bidders[key]
            i += 1
    
 
print(bidders)
print(f"The Winner is: {winner_name} with bid of {winner_price}")
    