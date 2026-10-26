from os import system as sys

sys("git status")
sys("git add .")
sys("git status")
sys("git log --oneline -3")
message = input("messeage: ")
if message == "":
    n = input("number: ")
    sys(f"git commit -m '{n}'")
else:
    sys(f"git commit -m '{message}'")
sys("git log --oneline -3")
check = input("everything's good: ")
if check in ["y", "Y", ""]:
    sys("git push")
