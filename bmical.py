run = True

while run:
    print("press enter or type 'exit' to exit")
    height_unit = input("measurement unit of hieght(cm or m)?: ")
    
    if height_unit == "exit" or height_unit == "":
        print("bye")
        run = False
    else:
        height = float(input("write your height in " + str(height_unit) + ": "))
        weight = int(input("write your wieght in kg: "))

    if height_unit == "cm":
        height = height / 100
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        print("bmi = " + str(bmi))
    elif height_unit == "m":
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        print("bmi = " + str(bmi))
