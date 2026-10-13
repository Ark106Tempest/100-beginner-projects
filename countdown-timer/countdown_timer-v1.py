import time

timer = int(input("1-60 second: "))

if timer > 0 and timer < 61:
    while timer > 0:
	    print(timer)
	    timer = timer - 1
	    time.sleep(1)
	    if timer == 0:
		    print("time over")
else:
    print("type in between 1-60")
