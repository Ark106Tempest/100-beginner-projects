year = int(input("enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("its a leap year")
else:
    print("its a normal year")

