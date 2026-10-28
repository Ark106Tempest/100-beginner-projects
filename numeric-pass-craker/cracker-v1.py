from pyzipper import AESZipFile as zf
file = zf("dummy.zip", 'r')

def pwd(length):
    tries = 0
    for i in range(10 ** length):
        i = str(i)
        zero = length - len(i)

        passwd = (("0" * zero) + i)
        try:
            file.setpassword(passwd.encode())
            file.read("secret.txt").decode()
            print(f"found the pass [{passwd}]")
            break
        except RuntimeError:
            tries += 1
n = int(input("length: "))
pwd(n)
