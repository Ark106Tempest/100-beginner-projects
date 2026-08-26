run = True
while run:
    print("1. calculate")
    print("2. exit")
    option = int(input("choose from the options above: "))
    if option == 1:
        numbers = []
        done = True
        while done:
            print("press enter for the average")
            num = input("enter the number: ")
            if num == "":
                done = False
            elif not num.isdigit():
                print("type a number")
            else:
                numbers.append(int(num))
                done = True
        print(sum(numbers) / len(numbers))
    elif option == 2:
        print("bye")
        run = False
    else:
        print("choose between the given options")
