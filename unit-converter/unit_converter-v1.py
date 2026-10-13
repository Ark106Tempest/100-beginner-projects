run = True
while run:
    print()
    print("===== UNIT CONVERTER =====")
    print()
    print("1. Distance")
    print("2. Temperature")
    print("3. weight")
    print("4. Exit")
    print()
    option = int(input("Choose from the options above: "))
    print()
    print()

    if option == 1:
        distance = True
        while distance:
            print("==== DISTANCE ====")
            print()
            print("1. Kilometers --> Miles")
            print("2. miles --> Kilometers")
            print("3. Back")
            print()
            d_option = int(input("Choose from the options above: "))
            print()
            print()

            if d_option == 1:
                kilometer = True
                while kilometer:
                    print("=== KILOMETERS --> MILES ===")
                    print()
                    print("type 'back' to go back")
                    km = input("Enter the distance: ")
                    if km == "back":
                        print()
                        kilometer = False
                    else:
                        km = float(km)
                        mi = km * 0.621371
                        mi = round(mi, 3)
                        print(f"{km}km is {mi}mi")
                        print()
            elif d_option == 2:
                mile = True
                while mile:
                    print("=== MILES --> KILOMETERS ===")
                    print()
                    print("type 'back' to go back")
                    mi = input("Enter the distance: ")
                    if mi == "back":
                        print()
                        mile = False
                    else:
                        mi = float(mi)
                        km = mi / 0.621371
                        km = round(km, 3)
                        print(f"{mi}mi is {km}km")
                        print()
            elif d_option == 3:
                distance = False
            else:
                print("something went wrong plz try again")
                print()
    elif option == 2:
        temperature = True
        while temperature:
            print("==== TEMPERATURE ====")
            print()
            print("1. Fahrenheit --> Celsuius")
            print("2. Celsius --> Fahrenheit")
            print("3. Back")
            print()
            t_option = int(input("choose from the options above: "))

            print()
            print()

            if t_option == 1:
                fahrenheit = True
                while fahrenheit:
                    print("=== FAHRENHEIT --> CELSIUS ===")
                    print()
                    print("type 'back' to go back")
                    f = input("Enter the temperature: ")
                    if f == "back":
                        print()
                        fahrenheit = False
                    else:
                        f = float(f)
                        c = (f - 32) * 5 / 9
                        c = round(c, 2)
                        print(f"{f}f is {c}c")
                        print()
            elif t_option == 2:
                celsius = True
                while celsius:
                    print("=== CELSIUS --> FAHRENHEIT ===")
                    print()
                    print("type 'back to go back")
                    c = input("Enter the temperature: ")
                    if c == "back":
                        print()
                        celsius = False
                    else:
                        c = float(c)
                        f = (c * 9 / 5) + 32
                        f = round(f, 2)
                        print(f"{c}c is {f}f")
                        print()
            elif t_option == 3:
                temperature = False
            else:
                print("something went wrong plz try again")
                print()
    elif option == 3:
        weight = True
        while weight:
            print("==== WEIGHT ====")
            print()
            print("1. Kilograms --> Pounds")
            print("2. Pounds --> Kilograms")
            print("3. Back")
            print()
            w_option = int(input("choose from the options above: "))

            print()
            print()

            if w_option == 1:
                kilogram = True
                while kilogram:
                    print("=== KILOGRAMS --> POUNDS ===")
                    print()
                    print("type 'back' to go back")
                    kg = input("Enter the weight: ")
                    if kg == "back":
                        print()
                        kilogram = False
                    else:
                        kg = float(kg)
                        lbs = kg * 2.20462
                        lbs = round(lbs, 3)
                        print(f"{kg}kg is {lbs}lbs")
                        print()
            elif w_option == 2:
                pound = True
                while pound:
                    print("=== POUNDS --> KILOGRAMS ===")
                    print()
                    print("type 'back' to go back")
                    lbs = input("Enter the weight: ")
                    if lbs == "back":
                        print()
                        pound = False
                    else:
                        lbs = float(lbs)
                        kg = lbs / 2.20462
                        kg = round(kg, 3)
                        print(f"{lbs}lbs is {kg}kg")
                        print()
            elif w_option == 3:
                weight = False
            else:
                print("something went wrong plz try again")
                print()
    elif option == 4:
        run = False
        print("Bye")
    else:
        print("somthing went wrong plz try again")
        print()
