import os
import random

def main():

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
    party_list = choose_names(party_list)

main()
