import os
import random

def prompt_user():

    print("1. Buy supplies")
    print("2. Stop to rest")
    print("3. Continue on the trail")
    user_action = input("Enter the number associated with the action you wish to take: ")

    return user_action

def rest(day):

    while True:

        days_to_rest = input("How many days do you want to rest? ")

        valid_inputs_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for valid_input in valid_inputs_list:

            if days_to_rest == valid_input:
                return day + int(days_to_rest)

        os.system("clear")
        print("Invalid input. Enter an integer between 1 and 10.")

def enter_town(inventory, cash, day):

    print("You have just arrived at a small town! What do you wish to do?")

    while True:

        user_action = prompt_user()

        if user_action == "1":
            inventory, cash = buy_supplies(inventory, cash)

        elif user_action == "2":
            day = rest(day)

        elif user_action == "3":
            distance_to_town = random.randint(100, 200)
            return inventory, cash, day, distance_to_town

        else:
            os.system("clear")
            print("Invalid input. Try again")
