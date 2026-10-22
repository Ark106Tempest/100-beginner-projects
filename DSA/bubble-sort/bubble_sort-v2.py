n = [2,5,8,3,4,7,9,1,6]
for _ in range(len(n) - 1):
    done = True
    for a in range(0, len(n) - 1):
        if n[a] > n[a + 1]:
            n[a], n[a + 1] = n[a + 1], n[a]
            done = False
    if done:
        break
print(n)
