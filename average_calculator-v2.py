numbers = []
done = True
while done:
    print("press enter for the average")
    num = input("enter the number: ")
    if num == "":
        done = False
    elif not num.isdigit():
        print("type a number")
    else:
        numbers.append(int(num))
        done = True
if num == "":
    print(sum(numbers) / len(numbers))

