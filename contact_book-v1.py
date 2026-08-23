contacts = [

]

run = True
while run:
    print("1. add")
    print("2. remove")
    print("3. view")
    print("4. exit")
    option = int(input("choose from the options above: "))

    if option == 1:
        number = input("write the contact number: ")
        name = input("write the contact name: ")
        
        contact = {"name": name, "number": number}

        contacts.append(contact)
        print("done")   
    elif option == 2:
        name = input("write the contact name you want to remove: ")
        number = input("write the contact number you want to remove: ")
        
        remove = {"name": name, "number": number}
        remove_index = contacts.index(remove)

        contacts.pop(remove_index)
        print("contact is removed")

    elif option == 3:
        print("ALL CONTACTS")
        num = len(contacts)
        count = 0
        for _ in range(num):
            contact = contacts[count]
            name = contact["name"]
            number = contact["number"]
            print(f"{name}; {number}")
            count += 1
    elif option == 4:
        print("bye")
        run = False
    elif option > 4 or option < 1:
        print("choose between the given option")
