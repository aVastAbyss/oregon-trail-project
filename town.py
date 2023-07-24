import os
import random

def prompt_user():

    while True:
        print("1. Buy supplies")
        print("2. Stop to rest")
        print("3. Continue on the trail")
        user_action = input("Select one of the above actions (1-3): ")

        return user_action

def buy_supplies(inventory, cash):

    costs = [250, 1, 1, 150, 25]
    item_names = ["1 oxen", "1 lb of food", "1 gallon of water", "1 spare part", "1 health pack"]

    while True:
        print("Gerald The ShopKeeper: Welcome to my shop! What would you like to buy?")
        print("1. Oxen")
        print("2. Food")
        print("3. Clean Water")
        print("4. Spare Parts")
        print("5. Medical Supplies")
        item_index = input("Select one of the above items (1-5): ")

        valid_inputs = ["1", "2", "3", "4", "5"]

        if item_index in valid_inputs:
            item_index = int(item_index)
            break

    print(item_names[item_index] + " costs $" + str(costs[item_index]))
    amount = input("What amount do you wish to buy? ")

def rest(day):

    while True:
        days_to_rest = input("How many days do you want to rest (1-10)? ")

        valid_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        if days_to_rest in valid_inputs:
            return day + int(days_to_rest)

        os.system("clear")
        print("Invalid input.")

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
            print("Invalid input.")
