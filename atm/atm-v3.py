balance = 0

run = True

while run:
    try:
        print("1: check balance")
        print("2: deposit")
        print("3: withdraw")
        print("4: exit")
        try:
            option = int(input("choose the options above [1,2,3,4]: "))
        except ValueError:
            print("valid numbers only!")
            continue
        if option == 1:
            print("current balance: " + str(balance))
        elif option == 2:
            try:
                deposit = int(input("enter amount: "))
            except ValueError:
                print("valid numbers only!")
                continue
            if deposit <= 0:
                print("minimum deposit amount 1rs!")
            else:
                balance = balance + deposit
                print(str(deposit) + "rs deposited successfully")
        elif option == 3:
            try:
                withdraw = int(input("enter amount: "))
            except ValueError:
                print("valid numbers only!")
                continue
            if withdraw < 1:
                print("minimum withdraw amount 1rs!")
            elif balance >= withdraw:
                balance = balance - withdraw
                print(str(withdraw) + "rs withdrew")
                print("collect the money from below")
            else:
                print("insufficient balance")
        elif option == 4:
            print("fuck off")
            run = False
        elif option > 4 or option < 1:
            print("pls choose between the given options")
    except KeyboardInterrupt:
        print("\nplz use built-in exit method")
