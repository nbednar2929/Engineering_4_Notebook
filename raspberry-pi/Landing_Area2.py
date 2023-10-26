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
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.circle import Circle

x = 0
y = 1

displayio.release_displays() #splits SCL SDA displays
sda_pin = board.GP14 #wiring up accelerometer
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP13) #identifies monitor
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def area(r1,r2,r3):
    c1 = [0,0]
    c2 = [0,0]
    c3 = [0,0]
    try:                    # Coordinate 1
        c1 = [int(o) for o in r1.split(",")] # Splits raw string: "1,2" into a string array: "1", "2", and turns each value into an int: 1,2
    except:
        print("Coordinate 1 Invalid, please enter in 'x,y' format")
        pass
    finally:

        try:                # Coordinate 2
            c2 = [int(o) for o in r2.split(",")]
        except:
            print("Coordinate 2 Invalid, please enter in 'x,y' format")
            pass
        finally:

            try:            # Coordinate 3
                c3 = [int(o) for o in r3.split(",")]
            except:
                print("Coordinate 3 Invalid, please enter in 'x,y' format")
                pass
            finally:
                A = (1/2)*abs(c1[x]*(c2[y] - c3[y]) + c2[x]*(c3[y] - c1[y]) + c3[x]*(c1[y] - c2[y])) # Easy plug and play equation for a triangle's area
                return A
                
while True:
    r1 = input("Coordinate 1: ")
    r2 = input("Coordinate 2: ")
    r3 = input("Coordinate 3: ")
    print("The Area of The Traingle With Vertices: (" + r1 + "), (" + r2 + "), (" + r3 + ") is " + area(r1,r2,r3) + " Square KM.")
