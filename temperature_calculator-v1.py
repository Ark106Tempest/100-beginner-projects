num = int(input("number of unit: "))
cvu = input("convert unit: ")
cvtu = input("converted unit: ")

if cvu == "c" and cvtu == "c":
	result = str(num)
	print(result + "c")
elif cvu == "c" and cvtu == "f":
	result = (num * 9/5) + 32
	result = str(result)
	print(result + "f")
elif cvu == "c" and cvtu == "k":
	result = num + 273.15
	result = str(result)
	print(result + "k")
elif cvu == "f" and cvtu == "c":
	result = (num - 32) * 5/9
	result = str(result)
	print(result + "c")
elif cvu == "f" and cvtu == "f":
	result = str(num)
	print(result + "f")
elif cvu == "f" and cvtu == "k":
	result = (num - 32) * 5/9 + 273.15
	result = str(result)
	print(result + "k")
elif cvu == "k" and cvtu == "c":
	result = num - 273.15
	result = str(result)
	print(result + "c")
elif cvu == "k" and cvtu == "f":
	result = (num - 273.15) * 9/5 + 32
	result = str(result)
	print(result + "f")
elif cvu == "k" and cvtu == "k":
	result = str(num)
	print(result + "k")
else:
	print("follow the fucking instructions")
