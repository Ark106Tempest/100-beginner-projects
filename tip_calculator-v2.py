bill = int(input("price of food: "))
tip = int(input("tip in % [popular: 5%, 10%, 25%]: "))

tip_amount = bill * (tip / 100)
t_amount = tip_amount + bill

split = input("would you like to split the bill [yes or no]: ")
if split == "yes":
    pp = int(input("how many people would you like to slpit the bill between?: "))
    p_person = t_amount / pp
    p_person = round(p_person, 2)
    print(str(p_person) + " is per person")
elif split == "no":
    print("alright your total is " + str(t_amount))

