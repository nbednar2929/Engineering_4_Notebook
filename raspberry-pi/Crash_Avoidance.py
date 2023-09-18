#type: ignore
import time
import board 
import digitalio 
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut,Direction,Pull
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c)

while True: 
    print("X Acceleration: " + (str(mpu.acceleration[0])))
    print("Y Acceleration: " + (str(mpu.acceleration[1])))
    print("Z Acceleration: " + (str(mpu.acceleration[2])))    
    print("Rotation: " + (str(mpu.gyro)))
    print("")
    time.sleep(1)