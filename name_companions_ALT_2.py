import random 
import os

def name_companions(party_list):
    index = 0
    while index != len(party_list):
        user_choice = input("Enter a name for a party member: ")
        if user_choice.isalpha():
            party_list[index]["name"] = user_choice
            index += 1
        else:
            pass
    os.system("clear")
    while True:
        print(f"""
        1. {party_list[0]["name"]}
        2. {party_list[1]["name"]}
        3. {party_list[2]["name"]}
        4. {party_list[3]["name"]}
        5. {party_list[4]["name"]}
        """)
        user_verify = input("Are these names correct? [Y/n] ")
        match user_verify:
            case "Y":
                break
            case "n":
                user_number = int(input("Enter the number that corresponds to the incorrect name: "))
                print(f"{user_number}.", party_list[user_number - 1]["name"])
                new_name = input("Enter a new name: ")
                party_list[user_number - 1]["name"] = new_name
                os.system("clear")
                continue
            case _:
                pass
    return party_list



member_1 = {"name": "", "health": 100}
member_2 = {"name": "", "health": 100}
member_3 = {"name": "", "health": 100}
member_4 = {"name": "", "health": 100}
member_5 = {"name": "", "health": 100}

party_list = [member_1, member_2, member_3, member_4, member_5]
party_list = name_companions(party_list)
