import time

minutes = int(input("minutes: "))
seconds = int(input("seconds: "))

while minutes > 0 or seconds > 0:
    print(str(minutes) + "m " + str(seconds) + "s")
    time.sleep(1)

    if seconds == 0:
        minutes = minutes - 1
        seconds = seconds + 59
    else:
        seconds = seconds - 1

print("Time Over")
