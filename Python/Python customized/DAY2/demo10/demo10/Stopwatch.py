import time

seconds = 0
minutes = 0
continued = 0
while continued != 1:
    print(minutes, ":", seconds)
    time.sleep(1)
    if seconds == 59:
        seconds = 0
        minutes = minutes + 1
    else:
        seconds = seconds + 1
