from time import sleep as sl
from random import uniform as uf
from random import choice as c

mv = ('L', 'R')
while True:
    sl(uf(0.50, 1))
    print(c(mv))
