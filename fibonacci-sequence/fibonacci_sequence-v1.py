num = 11
result = [0]
count = 1
for _ in range(1, num + 1):
    result.append(count)
    count = result[-1] + result[-2]
    if len(result) == num:
        break
print(result)
