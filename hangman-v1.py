from random import choice
words = ["freefire"]
run = True
while run:
    print("1. play")
    print("2. exit")
    option = int(input("choose from the options above: "))
    if option == 1:
        word = choice(words)
        found = []
        while True:
            display = ""
            for letter in word:
                if letter in found:
                    display += letter
                else:
                    display += "*"
            print("current word: ", display)
            if display == word:
                print("you guessed it")
                break
            letter = input("type a letter: ")
            letter = letter.lower()
            if letter in word:
                if letter not in found:
                    found.append(letter)
                else:
                    print("you already guessed it")
            else:
                print("not in the word")
    elif option == 2:
        print("bye")
        run = False
