run = True
while run:
    print("press enter or type 'exit' to exit")
    num = input("which multiplication table would you like to see: ")
    if num == "" or num == "exit":
        print("fuck off")
        run = False
    else:
        num = int(num)
        position = 1
        mid_pos = 1
        while position <= 10:
            for i in range(10):
                print(str(num) + " x " + str(mid_pos) + " = " + str(num * position))
                position = position + 1
                mid_pos = mid_pos + 1
