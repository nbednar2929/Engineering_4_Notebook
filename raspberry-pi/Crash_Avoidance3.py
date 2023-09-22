#type: ignore
#imports
import time
import board 
import digitalio 
import pwmio
from digitalio import DigitalInOut,Direction,Pull
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays() #splits SCL SDA displays

Green = digitalio.DigitalInOut(board.GP0) #initialize green led 
Green.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14 #wiring up accelerometer
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP13) #identifies monitor
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

#printing acceleration values
while True: 

    splash = displayio.Group() #displays and defines text
    title = f"ANGULAR VELOCITY: \n X:{str(round(mpu.gyro[0],3))} \n Y:{str(round(mpu.gyro[1],3))} \n Z:{str(round(mpu.gyro[2],3))}"
    text_area = label.Label(terminalio.FONT, text=title,color=0xFFFF00, x=5, y=5 )
    splash.append(text_area)
    display.show(splash)

    #print("X Acceleration: " + (str(mpu.acceleration[0])))
    #print("Y Acceleration: " + (str(mpu.acceleration[1])))
    #print("Z Acceleration: " + (str(mpu.acceleration[2])))    
    #print("Rotation: " + (str(mpu.gyro)))
    #print("")
    time.sleep(.1)

    if mpu.acceleration[0] >= 9 or mpu.acceleration[1] >= 9: #if gravity affects tilt 
        Green.value = True #led on
    elif mpu.acceleration[0] <= -9 or mpu.acceleration[1] <= -9: #if gravity tilt other way
            Green.value = True
    else: Green.value = False #else led false
