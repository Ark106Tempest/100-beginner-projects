run = True
while run:
    print("type 'exit' to exit")
    start = input("where to start from? press enter to start from 1: ")
    if start == "exit":
        run = False
    elif start == "":
        end = int(input("where to end?:"))
        start = 1
        while int(start) <= end:
            print(start)
            start = start + 1
    else:
        end = int(input("where to end?:"))
        while int(start) != end:
            print(str(start))
            start = int(start) + 1
