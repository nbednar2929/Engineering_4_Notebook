import time
import board # type: ignore
import digitalio # type: ignore

countdown = 10

while True: 
    countdown = countdown - 1
    if countdown < 0:
        countdown = 0
    print("Countdown: " + str(countdown))