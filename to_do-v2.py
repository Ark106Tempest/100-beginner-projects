todo = []

run = True

while run:
    print("")
    print("optiona we have")
    print("1. add")
    print("2. remove")
    print("3. view")
    print("4. exit")
    option = int(input("choose from the options above: "))
    if option == 1:
        task = input("write the task you want to add: ")
        todo.append(task)
    elif option == 2:
        r_task = input("write the task you want to remove: ")
        if r_task in todo:
            to_remove = todo.index(r_task)
            todo.pop(to_remove)
        elif r_task not in todo:
            print("there is no such task")
    elif option == 3:
        items = len(todo)
        item_num = 0
        point = 1
        for _ in range(items):
            print(f"{point}. {todo[item_num]}")
            item_num = item_num + 1
            point = point + 1
    elif option == 4:
        print("bye")
        run = False
    elif option > 4 or option < 1:
        print("choose in between the options")
