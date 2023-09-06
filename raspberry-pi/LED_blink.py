import time
import board # type: ignore
import digitalio # type: ignore

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

while True: 
    led.value = True
    time.sleep(.1)
    led.value =  False
    time.sleep(.1)