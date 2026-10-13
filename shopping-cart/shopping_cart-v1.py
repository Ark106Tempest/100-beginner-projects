items = {
        "names": [],
        "price": []
        }
run = True
while run:
    print("1. add item")
    print("2. remove item")
    print("3. view items")
    print("4. total price")
    print("5. exit")
    option = int(input("choose from the options above: "))
    if option == 1:
        add = True
        while add:
            print("type 'back' to go back")
            item_name = input("type the name of item: ")
            if item_name == "back":
                add = False
                break
            else:
                item_price = float(input("enter the price of item: "))
                items["names"].append(item_name)
                items["price"].append(item_price)
                print("product added successfully")
    elif option == 2:
        remove = True
        while remove:
            print("type 'back' to go back")
            item_name = input("type the name of the product: ")
            if item_name == "back":
                remove = False
                break
            else:
                item_price = float(input("type the price for verification: "))
                position = items["names"].index(item_name)
                items["names"].pop(position)
                items["price"].pop(position)
                print("product removed successfully")
    elif option == 3:
        for x in range(0, len(items["names"]), 1):
            name = items["names"][x]
            price = items["price"][x]
            print(f"{name}: ${price}")
    elif option == 4:
        total = 0
        for i in items["price"]:
            total += i
        print(f"your cart's total value is ${total}")
    elif option == 5:
        print("bye")
        run = False
