values = []
run = True
while run:
    print("1. sum")
    print("2. average")
    print("3. maximum")
    print("4. minimum")
    print("5. all")
    print("6. add values")
    print("7. exit")
    print("warning do not run the program empty!!!")
    option = int(input("choose from the options above: "))
    if option == 1:
        print(sum(values))
    elif option == 2:
        print(sum(values) / len(values))
    elif option == 3:
        print(max(values))
    elif option == 4:
        print(min(values))
    elif option == 5:
        print(sum(values))
        print(sum(values) / len(values))
        print(max(values))
        print(min(values))
    elif option == 6:
        done = True
        while done:
            print("press enter to end")
            num = input("enter the value: ")
            if num == "":
                done = False
            else:
                num = float(num)
                values.append(num)
    elif option == 7:
        print("bye")
        run = False
