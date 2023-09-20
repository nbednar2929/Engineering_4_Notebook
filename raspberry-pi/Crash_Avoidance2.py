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

#printing acceleration values
while True: 
    print("X Acceleration: " + (str(mpu.acceleration[0])))
    print("Y Acceleration: " + (str(mpu.acceleration[1])))
    print("Z Acceleration: " + (str(mpu.acceleration[2])))    
    print("Rotation: " + (str(mpu.gyro)))
    print("")
    time.sleep(1)
    if mpu.acceleration[0] >= 9 or mpu.acceleration[1] >= 9: #if gravity affects tilt 
        Green.value = True #led on
    elif mpu.acceleration[0] <= -9 or mpu.acceleration[1] <= -9: #if gravity tilt other way
            Green.value = True
    else: Green.value = False #else led false
