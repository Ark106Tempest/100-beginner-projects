from random import uniform as uf
from random import choice as c
from time import sleep as sl
mv = ("L", "R")
print("1. default")
print("2. time")
print("3. how-many")
option = int(input("choose from above: "))
if option == 1:
    for _ in range(100):
        sl(uf(0.75, 1.5))
        print(c(mv))
elif option == 2:
    seconds = float(input("second: "))
    minutes = float(input("minutes: "))
    if minutes > 0:
        seconds = seconds + minutes * 60
    while seconds > 0:
        delay = uf(0.75, 1.5)
        sl(delay)
        print(c(mv))
        seconds -= delay
elif option == 3:
    num = int(input("how many do you want: "))
    for _ in range(num):
        sl(uf(0.75, 1.5))
        print(c(mv))
else:
    print("plz try again")
