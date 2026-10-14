username = "tester"
password = "isitworking?"
uname = input("enter the username: ")
passwd = input("enter the password: ")
if uname == username:
    if passwd == password:
        print("welcome")
    else:
        print("forgot your password?")
        print("i dont give a fuck, so keep trying to remember it")
else:
    print("FUCK OFFF!! you impersonator!")
