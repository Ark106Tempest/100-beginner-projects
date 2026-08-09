from datetime import datetime

bday = int(input("enter you birthday: "))
year = datetime.now().year
print(f"you are {year - bday} years old")
