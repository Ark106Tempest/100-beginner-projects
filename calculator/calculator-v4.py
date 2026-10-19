def head(heading, length):
    print()
    print("=" * length, heading, "=" * length)
    print()

run = True
while run:
    head("CALCULATOR", 5)
    print("1. Calculate")
    print("2. Settings") # its corrently unavalable but in future ill add more fetures
    print("3. Exit")
    print()
    option = int(input("Choose from the options above: "))

    if option == 1:
        calculate = True
        while calculate:
            head("CALCULATE", 4)
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Back")
            print()
            cal = int(input("Choose from the option: "))

            if cal == 1:
                add = True
                while add:
                    head("ADDITION", 3)
                    print("Press enter to go back")
                    num1 = input("First number: ")
                    if num1 == "":
                        add = False
                    else:
                        num2 = input("Second number: ")
                        print(f"Final result is {float(num1) + float(num2)}")
            elif cal == 2:
                sub = True
                while sub:
                    head("SUBTRACTION", 3)
                    print("Press enter to go back")
                    num1 = input("First number: ")
                    if num1 == "":
                        sub = False
                    else:
                        num2 = input("Second number: ")
                        print(f"Final result is {float(num1) - float(num2)}")
            elif cal == 3:
                mul = True
                while mul:
                    head("MULTIPLICATION", 3)
                    print("Press enter to go back")
                    num1 = input("First number: ")
                    if num1 == "":
                        mul = False
                    else:
                        num2 = input("Second number: ")
                        print(f"Final result is {float(num1) * float(num2)}")
            elif cal == 4:
                div = True
                while div:
                    head("DIVISION", 3)
                    print("Press enter to go back")
                    num1 = input("First number: ")
                    if num1 == "":
                        div = False
                    else:
                        num2 = input("Second number: ")
                        if float(num2) == 0:
                            print("ARE YOU TRYING TO CRASH MY PROGRAM!!!!!")
                        else:
                            print(f"Final result is {round(float(num1) / float(num2),3)}")
            elif cal == 5:
                calculate = False
            else:
                print("something went wrong plz try again")
    elif option == 3:
        print("Bye")
        run = False
    
