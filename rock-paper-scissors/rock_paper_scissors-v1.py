from random import choice
from time import sleep
run = True
while run:
    print("1. play")
    print("2. exit")
    menu = int(input("chose the option above: "))
    if menu == 1:
        play = True
        while play:
            player = input("secrectly type your move: ")
            bot = choice(["rock","paper","scissors"])
            print("ready")
            sleep(0.5)
            print("set")
            sleep(0.5)
            print("go")
            sleep(1)
            if (player == "rock" and bot == "rock") or (player == "paper" and bot == "paper") or (player == "scissors" and bot == "scissors"):
                print("final result is...")
                sleep(1)
                print("bot's move is " + bot)
                print("its a tie")
            elif (player == "rock" and bot == "scissors") or (player == "scissors" and bot == "paper") or (player == "paper" and bot == "rock"):
                print("final result is...")
                sleep(1)
                print("bot's move is " + bot)
                print("you won")
            elif (player == "scissors" and bot == "rock") or (player == "rock" and bot == "paper") or (player == "paper" and bot == "scissors"):
                print("final result is...")
                sleep(1)
                print("bot's move is " + bot)
                print("you lose")
            print("whould you like to play again")
            print("press enter to play again and type 'back' to go back")
            do_something = True
            while do_something:
                again = input("what would you like to do?: ")
                if again == "":
                    play = True
                    do_something = False
                elif again == "back":
                    play = False
                    do_something = False
                else:
                    print("something went wrong plz try again")
                        
                
    elif menu == 2:
        print("fuck off")
        run = False
    else:
        print("something went wrong plz try again")
