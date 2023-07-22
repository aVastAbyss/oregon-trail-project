import os
import random

def main():

    current_trail_distance = 0
    distance_to_town = 0

    cash = 0
    inventory = {"oxen": 0,
                 "food": 0,
                 "clean water": 0,
                 "spare parts": 0,
                 "medical supplies": 0}

    person_1 = {"name": "",
                "health": 0}

    person_2 = {"name": "",
                "health": 0}

    person_3 = {"name": "",
                "health": 0}

    person_4 = {"name": "",
                "health": 0}

    person_5 = {"name": "",
                "health": 0}

    party_list = [person_1, person_2, person_3, person_4, person_5]

    cash = select_difficulty()
    party_list = name_companions(party_list)

    if distance_to_town == 0:
        inventory, distance_to_town = enter_town(inventory)

main()
