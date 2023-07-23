member_1 = {"name": "",
                "health": 0}

member_2 = {"name": "",
                "health": 0}

member_3 = {"name": "",
                "health": 0}

member_4 = {"name": "",
                "health": 0}

member_5 = {"name": "",
                "health": 0}

party_list = [member_1, member_2, member_3, member_4, member_5]

def name_companions(party_list):

    print("1. \n2. \n3. \n4. \n5.")

    changes_confirmed = False
    while changes_confirmed == False:
        
        member_1["name"] = input("What is the name of the party leader? ")
        print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])

        for member in party_list[1:]:
            member["name"] = input("What are the names of the other members of your party? ")
            print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])

        confirm_names = input("Are these names correct? (Y/N) ")
        if confirm_names == "Y" or confirm_names == "y" or confirm_names == "Yes" or confirm_names == "yes":
            changes_confirmed = True

        if confirm_names == "N" or confirm_names == "n" or confirm_names == "No" or confirm_names == "no":
            change_name = input("Which name is incorrect? (1-5) ")

            choices = {"1": input("What is the name of the party leader? "),
                       "2": input("What are the names of the other members of your party? "),
                       "3": input("What are the names of the other members of your party? "),
                       "4": input("What are the names of the other members of your party? "),
                       "5": input("What are the names of the other members of your party? ")}

            if choices = 

    print(party_list)
    return party_list




name_companions(party_list)
