num = float(input())
if num > 0:
    print("its a positive number")
elif num < 0:
    print("its a negative number")
else:
    print("its a neutral nuumber")
if (num % 2) == 0:
    print("its a even number")
else:
    print("its a odd number")
print(num*num, "is its square")
print(num**3, "is its cube")
if num.is_integer():
    print("its a integer")
else:
    print("its a decimal number")
