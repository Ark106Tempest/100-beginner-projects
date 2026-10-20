from math import isfinite as isf
from random import uniform as uf
from random import choice as c
from time import sleep as sl
run = True
diff_stat = "medium"
minimum = 1
maximum = 1.25
mv = ("L", "R")
while run:
    try:
        print(f"===Current diff - '{diff_stat}'===")
        print("1. default")
        print("2. time")
        print("3. how-many")
        print("4. difficulty")
        print("5. exit")
        try:
            option = int(input("choose from above: "))
        except ValueError:
            print("valid numbers only!")
            continue
        if option == 1:
            for _ in range(100):
                sl(uf(minimum, maximum))
                print(c(mv))
        elif option == 2:
            minutes = input("minutes ('enter' to skip): ")
            if minutes == "":
                minutes = 0
            else:
                try:
                    if int(minutes) < 0:
                        print("no reverse counting, fuck you")
                        continue
                    elif int(minutes) > 525600:
                        print("are you serius?")
                        continue
                    minutes = int(minutes)
                except ValueError:
                    print("valid numbers only!")
                    continue
            try:
                seconds = int(input("seconds: "))
                if seconds < 0:
                    print("FUCK YOU!!")
                    continue
                elif seconds > 59:
                    print("just use minutes, YOU MORON!")
                    continue
            except ValueError:
                print("valid numbers only!")
                continue
            seconds = seconds + minutes * 60
            while seconds > 0:
                delay = uf(minimum, maximum)
                sl(delay)
                print(c(mv))
                seconds -= delay
        elif option == 3:
            try:
                num = int(input("how many do you want: "))
                if num > 0:
                    print("ok.")
                elif num == 0:
                    print("bro wtf do you want me to even count")
                    continue
                else:
                    print("bro why the hell do you want me to count in reverse")
                    continue
            except ValueError:
                print("numbers only!")
                continue
            for _ in range(num):
                sl(uf(minimum, maximum))
                print(c(mv))
        elif option == 4:
            while True:
                print(f"===Current diff - '{diff_stat}'===")
                print("1. easy")
                print("2. medium")
                print("3. hard")
                print("4. extreme")
                print("5. custom")
                print("6. back")
                try:
                    diff = int(input("select difficulty: "))
                except ValueError:
                    print("valid numbers only!")
                    continue
                if diff == 1:
                    diff_stat = "easy"
                    minimum = 1.25
                    maximum = 1.5
                elif diff == 2:
                    diff_stat = "medium"
                    minimum = 1
                    maximum = 1.25
                elif diff == 3:
                    diff_stat = "hard"
                    minimum = 0.75
                    maximum = 1
                elif diff == 4:
                    diff_stat = "extreme"
                    minimum = 0.5
                    maximum = 0.75
                elif diff == 5:
                    try:
                        minn = float(input("minimum (lowest[0.25]): "))
                        if not isf(minn):
                            print("what?.....")
                            continue
                    except ValueError:
                        print("numbers only!")
                        continue
                    try:
                        maxx = float(input("maximum (highest[3.00]): "))
                        if not isf(maxx):
                            print("what the hell??..")
                            continue
                    except ValueError:
                        print("numbers only!")
                        continue
                    if minn > maxx or minn < 0.25 or maxx > 3:
                        print("something went wrong plz try again")
                        continue
                    else:
                        diff_stat = "custom"
                        minimum = minn
                        maximum = maxx
                        print("Done.")
                elif diff == 6:
                    break
                else:
                    print("try again")
        elif option == 5:
            run = False
            print("bye")
        else:
            print("plz try again")
    except KeyboardInterrupt:
        print("plz use built-in exit method")
