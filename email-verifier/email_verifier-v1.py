email = input("enter the email: ")
email = email.lower()
dot = email.find(".")
if "@" in email:
    if email[dot::] == ".com":
        print("valid email")
    else:
        print("invalid email")
else:
    print("invalid email")
