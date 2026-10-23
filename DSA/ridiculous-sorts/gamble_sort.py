from random import randint as ri

n = [2,6,1,7,8,4,5,3,9]

while True:
    a = ri(0, len(n) - 1)
    b = ri(0, len(n) - 1)
    if n[a] > n[b]:
        n[a], n[b] = n[b], n[a]
    count = 0
    for i in range(0, len(n) - 1):
        if n[i] < n[i + 1]:
            count += 1
    if count == len(n) - 1:
        break
print(n)
