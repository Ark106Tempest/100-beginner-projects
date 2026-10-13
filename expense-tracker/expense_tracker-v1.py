expenses = []
run = True
while run:
    print("1. add expense")
    print("2. view expense")
    print("3. total spent")
    print("4. search") # this is for future updates
    print("5. exit")
    option = int(input("choose from the options above: "))
    if option == 1:
        add = {
            "name": input("type the name of this expense: "),
            "cost": float(input("type the cost of this expense: "))
            }
        expenses.append(add)
        print("expense added")
    elif option == 2:
        num = len(expenses)
        count = 0
        for _ in range(num):
            expense = expenses[count]
            print(f"{expense['name']}: {expense['cost']}rs")
            count += 1
    elif option == 3:
        num = len(expenses)
        count = 0
        total = 0
        for _ in range(num):
            expense = expenses[count]
            total = total + float(expense['cost'])
        print(f"total is {total}")
    elif option == 4:
        print("this feature is currently unavailable")
    elif option == 5:
        print("bye")
        run = False
