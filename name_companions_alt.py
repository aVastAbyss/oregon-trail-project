def show_companion_names(party_list):

    os.system("clear")

    for name_index in range(len(party_list)):
        print(str(name_index + 1), party_list[name_index]["name"])

def validate_names():

    while True:
        is_names_correct = input("Are the above names correct (y/n)? ").lower()

        if is_names_correct == "y" or is_names_correct == "n":
            return is_names_correct

        print("Invalid input.")

def prompt_name_change(party_list):

    while True:
        name_index = input("Which name do you wish to change (1-5)? ")

        valid_inputs_list = ["1", "2", "3", "4", "5"]

        if name_index in valid_inputs_list:
            name_index = int(name_index) - 1
            break

        print("Invalid input.")

    party_list[name_index]["name"] = input("Enter a name: ")
    return party_list

def name_companions(party_list):

    for member_index in range(len(party_list)):
        show_companion_names(party_list)
        party_list[member_index]["name"] = input("Enter a name: ")

    while True:
        show_companion_names(party_list)

        if validate_names() == "y":
            return party_list

        party_list = prompt_name_change(party_list)
