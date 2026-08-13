from random import randint
run = True
while run:
    print("type 'exit' to exit")
    lenth = input("lenth of the pass (def = 8): ")
    if lenth == "exit":
        print("bye")
        run = False
    elif lenth == "":
        ps = ""
        for i in range(8):
            num = randint(0,9)
            ps = ps + str(num)
        print(ps)
    elif int(lenth) < 4:
        print("the password will be too short. choose a bigger number")
    else:
        ps = ""
        for i in range(int(lenth)):
            num = randint(0,9)
            ps = ps + str(num)
        print(ps)
