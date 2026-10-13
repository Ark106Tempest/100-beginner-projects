run =True
while run:
    print("1. percentage of a number")
    print("2. exit")
    option = int(input("choose the option above: "))
    if option == 1:
        start = True
        while start:
            number = int(input("enter the number: "))
            percentage = int(input("percentage you want to know: "))
            result = (percentage / 100) * number
            print(f"{percentage}% of {number} is {result}")
            back_option = input("press enter to do it again and type 'back' to go back: ")
            if back_option == "":
                print("ok")
            elif back_option == "back":
                print("ok")
                start = False
            else:
                print("something went wrong")
    elif option == 2:
        print("bye")
        run = False
    else:
        print("something went wrong")
