def change_difficulty():
    difficulty_prompt = print("""Choose from one of the difficulties below:
    1. Easy
    2. Medium
    3. Hard
    """)
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
