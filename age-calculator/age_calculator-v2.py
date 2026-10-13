from datetime import datetime
run = True
while run:
    print("press enter or type 'exit' to exit")
    bday = input("what year were you born?: ")
    year = datetime.now().year
    if bday == "" or bday == "exit":
        print("bye")
        run = False
    elif year < int(bday):
        print("something went wrong")
    else:
        print(f"you are {year - int(bday)} years old")

