from pyzipper import AESZipFile as zf
file = zf("dummy.zip", 'r')
target = file.getinfo("secret.txt")

def pwd(length):
    tries = 0
    for i in range(10 ** length):
        passwd = str(i).zfill(length)
        try:
            file.setpassword(passwd.encode())
            file.open(target)
            print(f"found the pass [{passwd}]")
            break
        except RuntimeError:
            tries += 1
n = int(input("length: "))
pwd(n)
