def change_difficulty():
    difficulty_prompt = """Choose who you are during the trail:
    1. Banker
    2. Farmer
    3. Carpenter
    """
    print(difficulty_prompt)
    user_choice = input("Choose a number corresponding to one of the options above: ")
    while True:
        match user_choice:
            case "1":
                cash = 6000
                break
            case "2":
                cash = 2500
                break
            case "3":
                cash = 1000
                break
            case _:
                os.system("clear")
                print(difficulty_prompt)
                user_choice = input("Please enter a valid number corresponding to one of the options above: ")
    return cash
