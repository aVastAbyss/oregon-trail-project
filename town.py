import os
import random

def prompt_user():

    print("1. Buy supplies")
    print("2. Stop to rest")
    print("3. Continue on the trail")
    user_action = input("Enter the number associated with the action you wish to take: ")

    return user_action

def enter_town(inventory, cash, day):

    print("You have just arrived at a small town! What do you wish to do?")

    while True:

        user_action = prompt_user()

        if user_action == "1":
            inventory, cash = buy_supplies(inventory, cash)

        elif user_action == "2":
            

        elif user_action == "3":
            distance_to_town = spawn_next_town()
            return inventory, cash, day, distance_to_town
    
        else:
            print("Invalid input. Try again")
    
        
