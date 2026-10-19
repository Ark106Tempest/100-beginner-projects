balance = 0
deposit = 0
withdraw = 0

print("1: check balance")
print("2: deposit")
print("3: withraw")
print("4: exit")

run = True

while run:
    try:
        option = int(input("choose the options above [1,2,3,4]: "))
    except ValueError:
        print("only numbers!")
        continue
    if option == 1:
        print("current balance " + str(balance))
    elif option == 2:
        try:
            deposit = int(input("enter amount: "))
        except valueError:
            print("only numbers!")
            continue
        balance = balance + deposit
        print(str(deposit) + "rs deposited successfully")
    elif option == 3:
        try:
            withdraw = int(input("enter amount: "))
        except ValueError:
            print("only numbers!")
            continue
        if balance >= withdraw:
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
