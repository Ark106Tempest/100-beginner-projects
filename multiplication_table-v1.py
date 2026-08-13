run = True

while run:
    print("press enter or type 'exit' to exit")
    num = input("which multiplication table would you like to see: ")
    if num == "" or num == "exit":
        print("fuck off you fucking bitch")
        run = False
    else:
        num = int(num)
        print(str(num) + " x 1 = " + str(num * 1))
        print(str(num) + " x 2 = " + str(num * 2))
        print(str(num) + " x 3 = " + str(num * 3))
        print(str(num) + " x 4 = " + str(num * 4))
        print(str(num) + " x 5 = " + str(num * 5))
        print(str(num) + " x 6 = " + str(num * 6))
        print(str(num) + " x 7 = " + str(num * 7))
        print(str(num) + " x 8 = " + str(num * 8))
        print(str(num) + " x 9 = " + str(num * 9))
        print(str(num) + " x 10 = " + str(num * 10))
