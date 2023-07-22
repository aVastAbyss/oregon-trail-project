def name_companions(party_list):

    print("1. \n2. \n3. \n4. \n5.")

    member_1["name"] = input("What is the name of the party leader? ")
    print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
    member_2["name"] = input("what are the names of the other members of your party? ")
    print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
    member_3["name"] = input("what are the names of the other members of your party? ")
    print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
    member_4["name"] = input("what are the names of the other members of your party? ")
    print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
    member_5["name"] = input("what are the names of the other members of your party? ")
    print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"]) 

    confirm_names = input("Are these names correct? \n (Y/N) ")
    
    if confirm_names == "Y" or confirm_names == "y" or confirm_names == "Yes" or confirm_names == "yes":
        return party_list
    
    if confirm_names == "N" or confirm_names == "n" or confirm_names == "No" or confirm_names == "no":
        change_name = input("Which name is incorrect? (1-5) ")

        if change_name == "1":
            member_1["name"] = input("What is the name of the party leader? ")
            print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
        if change_name == "2":
            member_2["name"] = input("what is their name? ")
            print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
        if change_name == "3":
            member_3["name"] = input("what is their name? ")
            print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
        if change_name == "4":
            member_4["name"] = input("what is their name? ")
            print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
        if change_name == "5":
            member_2["name"] = input("what is their name? ")
            print("1." + member_1["name"] + "\n2." + member_2["name"] + "\n3." + member_3["name"] + "\n4." + member_4["name"] + "\n5." + member_5["name"])
        
name_companions(party_list)
