#type: ignore
#imports
import time
import board 
import digitalio 
import pwmio
from digitalio import DigitalInOut,Direction,Pull
import adafruit_mpu6050
import busio

Green = digitalio.DigitalInOut(board.GP0) #initialize green led 
Green.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14 #wiring up accelerometer
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c) #initializing MPU

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
tilt = 0 

with open("/data.csv", "a") as datalog:
    #printing acceleration values
    led.value = True
    time.sleep(0.1)
    led.value = False
    while True: 
        datalog.write(f"{time.monotonic()},{mpu.acceleration[0]},{mpu.acceleration[2]},{mpu.acceleration[2]},{tilt}\n")
        datalog.flush()
        time.sleep(.9)
        if mpu.acceleration[0] >= 9 or mpu.acceleration[1] >= 9: #if gravity affects tilt 
            Green.value = True #led on
            tilt = 1
        elif mpu.acceleration[0] <= -9 or mpu.acceleration[1] <= -9: #if gravity tilt other way
            Green.value = True
            tilt = 0
        else: Green.value = False #else led false
