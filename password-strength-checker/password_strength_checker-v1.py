from string import ascii_lowercase, ascii_uppercase, digits, punctuation
lower = ascii_lowercase
upper = ascii_uppercase
num = digits
punch = punctuation
run = True
while run:
    print("1. check")
    print("2. exit")
    option = int(input("choose from the options above: "))
    if option == 1:
        password = input("to check the strength of a password\ntype your password here: ")
        words = len(password)
        if words < 4:
            print("dude its not even a password")
        elif words >= 4:
            count = 0
            lowercase = []
            uppercase = []
            digits = []
            punc = []
            for _ in range(words):
                letter = password[count]
                if letter in lower:
                    lowercase.append("1")
                elif letter in upper:
                    uppercase.append("1")
                elif letter in num:
                    digits.append("1")
                elif letter in punch:
                    punc.append("1")
                else:
                    print(f"what the hell is this {letter}")
                count += 1
            low = len(lowercase)
            up = len(uppercase)
            di = len(digits)
            pun = len(punc)
            conditions = [low >= 1, up >= 1, di >= 1, pun >= 1, words >= 8]
            total = sum(conditions)
            if total == 0:
                print("my ball hair is stonger than that")
            elif total == 1:
                print("very weak password. just quit man there is nothing you can do")
            elif total == 2:
                print("weak password but you can do better")
            elif total == 3:
                print("its fair i think")
            elif total == 4:
                print("its pretty good")
            elif total == 5:
                print("its amazing")
    elif option == 2:
        print("bye")
        run = False
    else:
        print("just use what is here. dont try to be oversmart")
