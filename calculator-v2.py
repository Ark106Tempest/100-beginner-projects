innum1 = int(input("first number: "))
wtd = input("what to do [+,-,*,/]: ")
innum2 = int(input("second number: "))

if wtd != "+" and wtd != "-" and wtd != "*" and wtd != "/":
	print("fuck you")

if wtd == "+":
	print(innum1 + innum2)
elif wtd == "-":
	print(innum1 - innum2)
elif wtd == "*":
	print(innum1 * innum2)
elif wtd == "/":
	print(innum1 / innum2)
