bill = int(input("price of food: "))
tip = int(input("tip in %: "))

tip_amount = bill * (tip / 100)
t_amount = tip_amount + bill

print("your total is " + str(t_amount))
