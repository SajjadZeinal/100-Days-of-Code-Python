# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:18:06 2022

@author: Sajjad

Day 10 project: Calculator
"""
#Calculator

import sys
sys.path.insert(1, "D:/100 Days of Code-Python/10/art")
import art
print(art.logo)

#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations={
    "+":add, 
    "-":subtract,
    "*":multiply,
    "/":divide
    }



def calculator():
    decision = "y"
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    while decision == "y":       
        for symbol in operations:
            print(symbol)    
        operation_symbol = input("Which operation you want to do? ")
        function = operations[operation_symbol]    
        answer = function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        decision = input("Do you want to continue with your current answer?(y/n) ")
        
        if decision == "y":
            num3 = int(input("What is your new number? "))
            num1 = answer
            num2= num3
        else:
            decision_2 = input("Do you want to restart calculator?(y/n)")
            if decision_2 == "y":
                calculator()
            else: 
                decision = "n"



calculator()


