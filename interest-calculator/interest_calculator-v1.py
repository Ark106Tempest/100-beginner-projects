amount = float(input("enter the base amount: "))
rate = float(input("enter the percent rate: "))
time = float(input("enter the time in years: "))
interest = (amount * rate * time) / 100
print("interest will be", interest)
print("total amount will be", amount + interest)
