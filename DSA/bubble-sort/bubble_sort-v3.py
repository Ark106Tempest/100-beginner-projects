n = [2,5,8,3,4,7,9,1,6]
swap = 0
for i in range(1, len(n) - 1):
    done = True
    for a in range(0, len(n) - i):
        if n[a] > n[a + 1]:
            n[a], n[a + 1] = n[a + 1], n[a]
            print(swap)
            swap += 1
            done = False
    if done:
        break
print(n)
