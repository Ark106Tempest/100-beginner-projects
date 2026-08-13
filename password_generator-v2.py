from random import randint
from random import choice
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation

lc = ascii_lowercase
uc = ascii_uppercase
num = digits
num = str(num)
pun = punctuation

run = True
while run:
    print("type 'exit' to exit")
    lenth = input("lenth of the pass (def = 8): ")
    if lenth == "exit":
        print("bye")
        run = False
    else:
        print("types [a = 1, A = 2, @ = 3, num = 4]")
        pass_type = input("which type of pass: ")
        ps = ""
        if lenth == "" and pass_type == "":
            print("umm.. you did not type anything?")
        else:
            pass_type = int(pass_type)
            if lenth == "" and pass_type == 1:
                for i in range(8):
                    character = choice(lc)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 2:
                for i in range(8):
                    character = choice(uc)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 3:
                for i in range(8):
                    character = choice(pun)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 4:
                for i in range(8):
                    character = choice(num)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 12:
                for i in range(8):
                    character = choice(lc + uc)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 13:
                for i in range(8):
                    character = choice(lc + pun)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 14:
                for i in range(8):
                    character = choice(lc + num)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 123:
                for i in range(8):
                    character = choice(lc + uc + pun)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 124:
                for i in range(8):
                    character = choice(lc + uc + num)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 134:
                for i in range(8):
                    character = choice(lc + pun + num)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 1234:
                for i in range(8):
                    character = choice(lc + uc + pun + num)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 23:
                for i in range(8):
                    character = choice(uc + pun)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 24:
                for i in range(8):
                    character = choice(uc + num)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 234:
                for i in range(8):
                    character = choice(uc + pun + num)
                    ps = ps + character
                print(ps)
            elif lenth == "" and pass_type == 34:
                for i in range(8):
                    character = choice(pun + num)
                    ps = ps + character
                print(ps)
             
            elif lenth != "":
                lenth = int(lenth)
                if lenth < 4:
                    print("pass will be too short")
                
                elif lenth >= 4 and pass_type == 1:
                    for i in range(lenth):
                        character = choice(lc)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 2:
                    for i in range(lenth):
                        character = choice(uc)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 3:
                    for i in range(lenth):
                        character = choice(pun)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 4:
                    for i in range(lenth):
                        character = choice(num)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4  and pass_type == 12:
                    for i in range(lenth):
                        character = choice(lc + uc)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 13:
                    for i in range(lenth):
                        character = choice(lc + pun)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 14:
                    for i in range(lenth):
                        character = choice(lc + num)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 123:
                    for i in range(lenth):
                        character = choice(lc + uc + pun)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 124:
                    for i in range(lenth):
                        character = choice(lc + uc + num)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 134:
                    for i in range(lenth):
                        character = choice(lc + pun + num)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 1234:
                    for i in range(lenth):
                        character = choice(lc + uc + pun + num)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 23:
                    for i in range(lenth):
                        character = choice(uc + pun)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 24:
                    for i in range(lenth):
                        character = choice(uc + num)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 234:
                    for i in range(lenth):
                        character = choice(uc + pun + num)
                        ps = ps + character
                    print(ps)
                elif lenth >= 4 and pass_type == 34:
                    for i in range(lenth):
                        character = choice(pun + num)
                        ps = ps + character
                    print(ps)
