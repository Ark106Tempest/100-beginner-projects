from random import uniform as uf
from random import choice as c
from time import sleep as sl
run = True
minimum = 1
maximum = 1.25
mv = ("L", "R")
while run:
    print("1. default")
    print("2. time")
    print("3. how-many")
    print("4. difficulty")
    print("5. exit")
    option = int(input("choose from above: "))
    if option == 1:
        for _ in range(100):
            sl(uf(minimum, maximum))
            print(c(mv))
    elif option == 2:
        seconds = float(input("second: "))
        minutes = float(input("minutes: "))
        if minutes > 0:
            seconds = seconds + minutes * 60
        while seconds > 0:
            delay = uf(minimum, maximum)
            sl(delay)
            print(c(mv))
            seconds -= delay
    elif option == 3:
        num = int(input("how many do you want: "))
        for _ in range(num):
            sl(uf(minimum, maximum))
            print(c(mv))
    elif option == 4:
        print("1. easy")
        print("2. medium")
        print("3. hard")
        print("4. extreme")
        diff = int(input("select difficulty: "))
        if diff == 1:
            minimum = 1.25
            maximum = 1.5
        elif diff == 2:
            minimum = 1
            maximum = 1.25
        elif diff == 3:
            minimum = 0.75
            maximum = 1
        elif diff == 4:
            minimum = 0.5
            maximum = 0.75
        else:
            print("try again")
    elif option == 5:
        run = False
        print("bye")
    else:
        print("plz try again")
