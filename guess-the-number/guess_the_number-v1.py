from random import randint
run = True
while run:
    print("type 'exit' to exit")
    play = input("press enter to play: ")
    if play == "exit":
        print("bye")
        run = False
    elif play == "":
        back = True
        while back:
            num = randint(1, 10)
            guess = input("guess a number between 1 to 10: ")
            if guess == "back":
                back = False
            elif int(guess) == num:
                print(f"answer was {num}, you won!")
            else:
                print(f"answer was {num}, you lost")
