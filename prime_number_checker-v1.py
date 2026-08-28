num = 17
result = "its a prime number"
for i in range(2, num):
    if num % i == 0:
        result = "its not a prime number"
        break
print(result)
