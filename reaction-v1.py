from time import sleep as sl
from random import choice as c

mv = ('L', 'R')
while True:
    sl(0.75)
    print(c(mv))
