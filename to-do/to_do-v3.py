run = True
while run:
    print("\noptions we have")
    print("1. add")
    print("2. remove")
    print("3. view")
    print("4. exit")
    option = int(input("choose from the options above: "))
    if option == 1:
        task = input("write the task you want to add: ")
        with open("savetask.txt", "a") as file:
            file.write(task + "\n")
    elif option == 2:
        r_task = input("write the task you want to remove: ")
        with open("savetask.txt", "r") as file:
            lines = file.readlines()
        stripped = [line.strip() for line in lines]

        if r_task not in stripped:
            print("there is no such task")
        else:
            with open("savetask.txt", "w") as file:
                for line in lines:
                    if line.strip() != r_task:
                        file.write(line)
    elif option == 3:
        with open("savetask.txt", "r") as file:
            line_num = 1
            for line in file:
                print(f"{line_num}. {line.strip()}")
                line_num += 1
    elif option == 4:
        print("bye")
        run = False
    elif option > 4 or option < 1:
        print("choose in between the options")
