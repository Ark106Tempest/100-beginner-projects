run = True

while run:
    print("press enter or type 'exit' to exit")

    num1 = input("first number: ")
    if num1 == "" or num1 == "exit":
        run = False
    else:
        num2 = int(input("second number: "))
        num1 = int(num1)
        lcm = max(num1, num2)

        done = True
        while done:
            cp1 = lcm % num1
            cp2 = lcm % num2
            if cp1 == 0 and cp2 == 0:
                print(lcm)
                done = False
            else:
                lcm = lcm + 1
