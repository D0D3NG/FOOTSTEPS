# GAME LOOP BASE ON YOUR CHOICE

def game():
    #using while loops for the game loop, conditionals based on player choices and \n for aesthetic interface
    while True:
        print("\nHello and welcome to FOOTSTEPS!!\n\nA quick thinking choice game where you have to run away from someone or something!\n\n===== MAIN MENU =====\n 1. Start game\n 2. Exit\n")
        choice =  input("> ")

        # using ifs and else conditionals base on user prompt
        if choice == "1":
            game = input("\nYou heard some footsteps in the house. What do you do?\n1. run\n2. hide\n\n> ")
            # gameplay loop 1 and ending 1
            if game == "1":
                print("\nYou ran towards the light and broke out of the window. The end\n\n===GAME COMPLETE===")
                break
            # game loop 2 if user decides to hide instead
            elif game =="2":
                gameloop1 = input("\nyou hide inside a closet and the footsteps go past you\n1. Get out\n2. Remain hidden\n\n> ")
                if gameloop1 == "1":
                    gameloop2 = input("\nYou heard the footsteps again but this time it's rapid and loud. What do you do?\n1. run\n2. hide\n\n> ")
                    # similar to ending 1 escaping narrowly
                    if gameloop2 == "1":
                        print("\nYou ran towards the light and broke out of the window. The end\n\n===GAME COMPLETE===")
                        break
                    elif gameloop2 == "2":
                        print("\nYou tried to get back into the closet but an invisible force pulled you and drag you away into the darkness\n\n===GAME OVER===")
                        break
                # if the player decides to just hide the monster would get him thus a bad ending
                elif gameloop1 =="2":
                    print("\nThe footsteps return in blinding speed as the closet opens and something caught you.\n\n===GAME OVER===")
                    break
        # if user chooses to exit the game
        elif choice =="2":
            print("\nClosing game......\nBye-bye!!")
            break
        # if user chooses to not put the correct input
        else:
            print("Invalid, please try again")

game()