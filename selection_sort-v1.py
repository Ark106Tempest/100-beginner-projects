num = [6,8,4,9,2,3,1,5,7]
for x in range(0, len(num), 1):
    while True:
        def y_num():
            smallest = x
            for y in range(len(num) - 1, x, -1):
                if num[smallest] > num[y]:
                    smallest = y
            num[x], num[smallest] = num[smallest], num[x]
        before = num.copy()
        y_num()
        if before == num:
            break
print(num)
