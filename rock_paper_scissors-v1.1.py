from random import choice
from time import sleep
run = True
while run:
    print("1. play\n2. settings\n3. exit")
    menu = int(input("choose from the options above: "))
    if menu == 1:
        mode = True
        while mode:
            print("1. normal mode\n2. flow mode\n3. kid mode\n4. selective rounds\n5. back") #option 2,3 and 4 are currently unavailable
            option = int(input("select the game mode: "))
            if option == 1:
                play = True
                while play:
                    player = input("type your move secrectly: ")
                    bot = choice(["rock","paper","scissors"])
                    print("ready")
                    sleep(0.5)
                    print("set")
                    sleep(0.5)
                    print("go")
                    sleep(0.5)
                    print("final result is...")
                    sleep(1)
                    print(f"bot's move is {bot}")
                    if (player == "rock" and bot == "rock") or (player == "paper" and bot == "paper") or (player == "scissors" and bot == "scissors"):
                        print("ita a tie")
                    elif (player == "rock" and bot == "paper") or (player == "paper" and bot == "scissors") or (player == "scissors" and bot == "rock"):
                        print("you have lost")
                    elif (player == "rock" and bot == "scissors") or (player == "paper" and bot == "scissors") or (player == "scissors" and bot == "paper"):
                        print("you have won")
                    print("would you like to play again \npress enter to play again or type 'back' to go back")
                    dicision = True
                    while dicision:
                        again = input("what would you like to do?: ")
                        if again == "":
                            play = True
                            dicision = False
                        elif again == "back":
                            play = False
                            dicision = False
                        else:
                            print("something went wrong plz try again")
            elif option == 2:
                print("this option is currently unavailable")
            elif option == 3:
                print("this option is currently unavailable")
            elif option == 4:
                print("this option is currently unavailable")
            elif option == 5:
                mode = False
            else:
                print("something went wrong plz try again")
    elif menu == 2:
        print("this option is currently unavailable")
    elif menu == 3:
        print("bye")
        run = False
