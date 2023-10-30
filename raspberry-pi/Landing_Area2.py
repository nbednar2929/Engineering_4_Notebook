#type: ignore
#imports
import time
import board 
from digitalio import DigitalInOut,Direction,Pull
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

x = 0
y = 1

displayio.release_displays() #splits SCL SDA displays
sda_pin = board.GP14 #wiring pins
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) #identify display
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP13) #identifies monitor
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

c1 = [0,0] #creates coordinates 
c2 = [0,0]
c3 = [0,0]

def area(r1,r2,r3): #area function
    global c1
    global c2
    global c3
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
    
splash = displayio.Group() #displays and defines text
xline = Line(64,0,64,64,color=0xFFFF00) #x and y lines
yline = Line(0,32,128,32,color=0xFFFF00)
circle = Circle(64,32,2,outline=0xFFFF00) #origin
splash.append(xline)
splash.append(yline)
splash.append(circle)
display.show(splash) #show display

while True:
    r1 = input("Coordinate 1: ") #print coordinates
    r2 = input("Coordinate 2: ")
    r3 = input("Coordinate 3: ")
    print("The Area of The Traingle With Vertices: (" + str(r1) + "), (" + str(r2) + "), (" + str(r3) + ") is " + str(area(r1,r2,r3)) + " Square KM.") #print area

    triangle = Triangle(c1[x]+64,c1[y]+32,c2[x]+64,c2[y]+32,c3[x]+64,c3[y]+32,outline=0xFFFF00)#display triangle
    splash.append(triangle)
    display.show(splash)
