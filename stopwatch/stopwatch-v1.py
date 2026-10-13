from time import sleep
import select
import sys
run = True
while run:
    print("1. start")
    print("2. resume")
    print("3. reset")
    print("type 'exit' to exit")
    print("enter to stop")
    option = input("chose the option from above: ")
    if int(option) == 1:
        minutes = 0
        seconds = 0
        start = True
        while start:
            print(str(minutes) + ":" + str(seconds))
            if select.select([sys.stdin],[], [], 0)[0]:
                stop = input()
                if stop == "":
                    start = False
            sleep(1)

            if seconds == 59:
                minutes = minutes + 1
                seconds = seconds - 59
            else:
                seconds = seconds + 1
    elif int(option) == 2:
        start = True
        while start:
            print(str(minutes) + ":" + str(seconds))
            if select.select([sys.stdin],[], [], 0)[0]:
                stop = input()
                if stop == "":
                    start = False
            sleep(1)
            if seconds == 59:
                minutes = minutes + 1
                seconds = seconds - 59
            else:
                seconds = seconds + 1
    elif int(option) == 3:
        minutes = 0
        seconds = 0
    elif option == "exit":
        run = False
