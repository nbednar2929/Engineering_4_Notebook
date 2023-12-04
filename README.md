[Data Storage.csv](https://github.com/nbednar2929/Engineering_4_Notebook/files/13336374/Data.Storage.csv)# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch Pad Part 1](#launch-pad-part-1)
* [Launch Pad Part 2](#launch-pad-part-2)
* [Launch Pad Part 3](#launch-pad-part-3)
* [Launch Pad Part 4](#launch-pad-part-4)
* [Crash Avoidance Part 1](#crash-avoidance-part-1)
* [Crash Avoidance Part 2](#crash-avoidance-part-2)
* [Crash Avoidance Part 3](#crash-avoidance-part-3)
* [FEA Beam Part 1](#FEA-Beam-Part-1)
* [FEA Beam Part 2](#FEA-Beam-Part-2)
* [FEA Beam Part 3](#FEA-Beam-Part-3)
* [Landing Area Part 1](#Landing-Area-Part-1)
* [Landing Area Part 2](#Landing-Area-Part-2)
* [Morse Code Part 1](#Morse-Code-Part-1)
* [Morse Code Part 2](#Morse-Code-Part-2)
* [Data Storage](#Data-Storage)
* [Data Analysis](#Data-Analysis)
* [Raspberry Pi Assignment Template](#raspberry_pi_assignment_template)
* [Onshape Assignment Template](#onshape_assignment_template)

### Launch Pad Part 1

We were instructed to print a countdown from 10 to 0 to our serial monitor and then print "Liftoff" when you reach zero.

### Evidence 

https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/f7809c44-0927-4fc5-9968-a9e7f983bd40
    
### Wiring

There was no wiring for this assignment.

### Code

``` python
import time
import board # type: ignore
import digitalio # type: ignore

for i in range (10,0,-1): #for loop from 10 to 0 counting by 1
    print(i) #prints counter
    time.sleep(1) # 1 second delay
print("Liftoff") #print liftoff at the end of the countdown
```

### Reflection

This was a fairly basic assignment to get us back into the swing of things. I originally took a more convoluted approach to this assignment creating a "countdown" variable which wasn't nearly as concise as my final product after a bit of inspiration from my peers.

## Launch Pad Part 2

### Assignment Description

Wire two LEDs, a red one to blink every second and a green one to turn on when you have liftoff.

### Evidence 

https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/8bce27e9-6922-4650-96eb-75fd628076b5

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>
    
![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/b624ef84-7c64-48a6-894d-d1bc0a5c1d06)

</p>

</details>

### Code

``` python
#type: ignore
import time
import board 
import digitalio 

Red = digitalio.DigitalInOut(board.GP1) #initialize red led 
Red.direction = digitalio.Direction.OUTPUT
Green = digitalio.DigitalInOut(board.GP0) #initialize green led 
Green.direction = digitalio.Direction.OUTPUT

for i in range (10,0,-1): #for loop from 10 to 0 counting by 1
    print(i) #prints counter
    Red.value = True #turn red led on
    time.sleep(.2)
    Red.value = False #turn red led off
    time.sleep(.8) # 1 second delay    
print("Liftoff") #print liftoff at the end of the countdown
Green.value = True #turn on green led for 5 seconds
time.sleep(5)
```

### Reflection

This assignment was also pretty easy since we were just building off of part 1. All I had to do was initialize two LEDs and turn on the Red LED in the "for loop". The one difficult part was realizing I needed to add a sleep after turning on the Green LED or else it would instantly reset and never turn on.

## Launch Pad Part 3

### Assignment Description

Wire a button that when pressed starts the 10 second count down.

### Evidence 

https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/5c82c4e8-0767-460a-b7c3-e7e141390442

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>
    
![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/b479a5e4-39be-45b6-9e9b-b3f3f5cd9062)

</p>

</details>

### Code

```python
#type: ignore
import time
import board 
import digitalio 

Red = digitalio.DigitalInOut(board.GP1) #initialize red led 
Red.direction = digitalio.Direction.OUTPUT
Green = digitalio.DigitalInOut(board.GP0) #initialize green led 
Green.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP28) #initialize button
button.pull = digitalio.Pull.DOWN #pull button down
button.direction = digitalio.Direction.INPUT

while button.value == False: #when button is pressed
    time.sleep(0.3)

for i in range (10,0,-1): #for loop from 10 to 0 counting by 1
    print(i) #prints counter
    Red.value = True #turn red led on
    time.sleep(.2)
    Red.value = False #turn red led off
    time.sleep(.8) # 1 second delay    
print("Liftoff") #print liftoff at the end of the countdown
Green.value = True #turn on green led for 5 seconds
time.sleep(5)
```

### Reflection

For some reason pulling my button up didn't work so I had to do a bit of guess and check with rewiring my button and messing with my while loop until eventually everything alligned and the button started the countdown. I struggled to understand the difference between pulling it up and down, but thankfully I asked a friend who explained it to me.

## Launch Pad Part 4

### Assignment Description

At liftoff make a 180 degree servo spin 180 degrees.

### Evidence 

![ezgif com-optimize (1)](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/8a83edca-7464-4fff-b2c2-8c705d230505)

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>
    
![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/4a335aaf-2bcd-4c23-8099-ff090f3fac06)

</p>

</details>

### Code

``` python
#type: ignore
import time
import board 
import digitalio 
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut,Direction,Pull

pwm = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

Red = digitalio.DigitalInOut(board.GP1) #initialize red led 
Red.direction = digitalio.Direction.OUTPUT
Green = digitalio.DigitalInOut(board.GP0) #initialize green led 
Green.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP28) #initialize button
button.pull = digitalio.Pull.DOWN #pull button down
button.direction = digitalio.Direction.INPUT

while button.value == False: #when button is pressed
    time.sleep(0.3)

for i in range (10,0,-1): #for loop from 10 to 0 counting by 1
    print(i) #prints counter
    Red.value = True #turn red led on
    time.sleep(.2)
    Red.value = False #turn red led off
    time.sleep(.8) # 1 second delay    
print("Liftoff") #print liftoff at the end of the countdown
for angle in range(0, 185, 5):  # 0 - 180 degrees, 5 degrees at a time forward.
    my_servo.angle = angle
    print(angle)
    time.sleep(0.05)
Green.value = True #turn on green led for 5 seconds
time.sleep(5)
```

### Reflection

For this assignment I had to use a "for" loop which is something I've struggled with in the past. I had to lower the range of the for loop from 10-1 to 10-0 in order to get the loop to count down to 1 rather than 2 since for loops don't count the minimum of the range. I also multiple times had messed up which direction to put my LEDs into my breadboard. I had to realize that the LED has a flat edge around the outside. The wire that comes out of that flat edge connects to a negative pin.

## Crash Avoidance Part 1

### Assignment Description

Wire up an accelerometer that returns acceleration values for the x, y, and z axes to the serial monitor.

### Evidence 

![Crash Avoidance Part 1](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/6ffde8d8-b556-49e2-ad34-ca152541addb)

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>
    
![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/773750be-81d1-4f58-879c-50e8f393dc61)

</p>

</details>

### Code

```python
#type: ignore
import time #imports 
import board 
import digitalio 
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut,Direction,Pull
import adafruit_mpu6050
import busio

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
```

### Reflection

My only issues with this assignment was my serial monitor. I kept getting error messages when I had the line "print("X Acceleration:" + mpu.acceleration[0])". To fix this I added str infront of my acceleration value and put it in parenthesis. After that I had no more error messages and it printed how I wanted it to. So when you have text and a value to print you need to add "str" infront of your value for it to work.

## Crash Avoidance Part 2

### Assignment Description

Use acceleration values to trigger a warning light if the pico is tilted 90 degrees and set up your RPi Pico to run “headless” (not attached to a computer).

### Evidence 

![ezgif com-crop (1)](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/611d9102-8312-4090-b4be-dcc41a3fd7a4)

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>
    
![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/e271fb45-fc40-47b2-a57b-e41226dfc5ca)

</p>

</details>

### Code

```python
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
```

### Reflection

In my original code I only had the if statement "if mpu.acceleration[0] >= 9 or mpu.acceleration[1] >= 9:". Because of that if I tilted my breadboard one way the light would turn on, but if I turned it the other way the acceleration value would actually be negative and so the light wouldn't turn on. To fix this I had to add a second line which turned the led on if the value was less than -9. From now on I know to understand negative acceleration and to account for it when writing code.

## Crash Avoidance Part 3

### Assignment Description

Add an onboard OLED screen to print live angular velocity values.

### Evidence 

https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/9b9da6a6-fdb4-4143-b6ae-a5a5752a2791

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>
    
![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/e8f752da-b980-43a0-86c0-4e68a2858f71)

</p>

</details>

### Code

```python
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
```

### Reflection

I had two main issues with this assignment. The first is that I originally didn't have the line "displayio.release_displays()" at the top of my code right below my imports. As a result my OLED display couldn't be idenitified and wouldn't print my angular velocity. To fix this all I did was move that line to right below my imports. The second issue I had was with my syntax when printing on the OLED display. I tried to use my usual priting with strings and plus signs, but because of that all of my code was on one line and went off the screen of the OLED. To fix this I created an f string which I printed to my OLED display. I used "\n" to put my value on new lines, and seperated my values using "mpu.gyro[x]", x being either 0, 1, or 2. I also had to learn how to round the values by surrounding my values with parenthesis, on the left side of my values I wrote "round" and on the right side I put a comma and then the number of digits I'd like to round to. Once I added all of my newfound "f string" knowledge my value displayed wonderfully. (I can do whatever I can dream!)

## FEA Beam Part 1

### Assignment Description

Create a beam that can hold as much weight as possible while still following all of the assignments constraints.

### Part Link 

[Link To Beam](https://cvilleschools.onshape.com/documents/8bb0d31d162d28dc9f991ea0/w/fe1197780904e4d1d1386b24/e/ca967a76187dc0c5098b74f0?renderMode=0&uiState=651d663d66bcfe34cbaa2349).

### Part Image

![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/105ef470-8152-4ce7-ae7f-e3294ce4fd50)

### Reflection

The biggest struggle for this assignment was having a starting point and getting the weight down to 13 grams. When it came to how I got a starting point I don't really know. I did a bit of research into beam theory, but it didn't really help all that much. I ended up just drawing some lines without much thought. For having to get it down to 13g all I did was just make a bunch of holes. I used triangles because they fit the angle requirements for printing and just made a pattern I thought looked cool. I added triangle after triangle until I got down to the final weight of 12.89g.

## FEA Beam Part 2

### Assignment Description

Render and analyze force and deflection plots of your beam and think how to improve your design.

### Part Link 

[Link To Part](https://cvilleschools.onshape.com/documents/8bb0d31d162d28dc9f991ea0/w/fe1197780904e4d1d1386b24/e/3e53c58bec7aca61a13eb0a7?renderMode=0&uiState=651f6751e920cb089592164c).

### Part Image

![old beam psi](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/d2153ce2-1e13-4d53-81cb-47b457737f58)
![old beam displacement](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/79a6c5ea-4d05-41b5-95b8-409da07e9aa4)

### Reflection

Me and Afton made two seperate designs and after analyzing the force plots of each of our desgins we decided to choose Afton's to continute with. His design not only is much easier to print but it weighs less meaning we have more room to add onto his design if we see fit. The most fragile piece of Afton's beam is the edges right along the attachment block. Our idea to reinforce that area is to add more supports that continue down the shaft of the beam.

## FEA Beam Part 3

### Assignment Description

Make actual physical imporvments to your beam based on the plots you rendered.

### Part Link 

[Link To Part](https://cvilleschools.onshape.com/documents/8bb0d31d162d28dc9f991ea0/w/fe1197780904e4d1d1386b24/e/3e53c58bec7aca61a13eb0a7)

### Part Image

![BRIDGEEEEEEEEEE](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/91f8f0ac-801b-4d9d-8dff-486c955610ae)
![BRIDGEEEEE](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/808c92dc-917c-4de0-8e53-6d5c24fb3e78)

### Reflection

The original "lowercase i beam" design was relatively strong but it had quite a lot of stress along the top of the beam. To try and reduce this I added supports on the sides of the top circle to try and gold some of the weight. This worked well at lowering the top stress to manageable levels, but the pressure was now concentrated at the base of the beam. I changed the "shrink factor" which made the end of the beam smaller to reduce weight as the middle and end of the beam don't have to bear much load and therefore shouldn't weigh much. This allowed me the extra material to fillet the base of the beam, which drastically improved the pressure, though there are still "hotspots" that have high stress.

## Landing Area Part 1

### Assignment Description

Write a script that takes three coordinates and returns the area using a function while also detecting errors in coordinate syntax.

### Evidence 

![landing area part 1](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/a5589f58-ab1b-4690-b5b6-72951a54c752)

### Wiring

No wiring was needed for this assignment.

### Code

```python
I used large portions of Afton's work in this assignment. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook
from time import sleep

x = 0
y = 1

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
    print(area(r1,r2,r3))
#credit to Afton Van Hooser

```

### Reflection

This assignment was really difficult to me, mainly given the fact that I had a bunch of other work this week and this assignment just felt big and overwhelming. I ended up using Afton's code, but I've spent lots of time reading it so I at the least understand what it means. I've learned from this assignment to go to sleep earlier and to try to break down my assignment into smaller segments so they feel less overwhelming. I used large portions of Afton's work in this assignment. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook

## Landing Area Part 2

### Assignment Description

Print an triangle on your OLED display using inputted coordinates. Also calculate and print the triangle's area on your terminal.

### Evidence 

![Landing Area Part 2](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/6f6479e1-11f1-4ff6-a4c5-01fff520e6db)

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>   
![landing area 2 ](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/cff2b737-2c9a-4d14-9bbe-5634ecfe1c8a)
</p>

</details>

### Code

```python
I used large portions of Afton's work in this assignment. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook
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
```

### Reflection

This assignment had a couple hiccups mainly on the code formatting side of things. The biggest fix for me was that my x and y axes were in my while loop, so when I input my traingle it would only show up for a split second before being erased and covered up by my axes. To fix this I took the lines of code about the axes out of the while loop and it fixed the issue. The other issue was needing to call c1, c2,and c3 outside of the area function. To fix this I got some help from Afton who told me that if I wrote "global" in front of them it would allow me to call them outside of the function. I also had to define them outside the function so making them global wouldn't cause an error. This is a continuation from the previous assignment which I used large portions of Afton's code. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook.

## Morse Code Part 1

### Assignment Description

Translate inputted text into morse code in your terminal

### Evidence 

![morse code part 1](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/40eb49e0-8587-456d-8559-5b95094eae56)

### Wiring

No wiring was required for this assignment.

### Code

```python
I used large portions of Afton's work in this assignment. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook
#type: ignore
#imports
import time 

#morse code library
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True: 
    #lowercases letters
    message = input("Your Message: ").upper()
    #defins message
    tmessage = ""
    #exits code if "-q" is tpyed
    if "-Q" in message:
        break
    #for loop with message
    for letter in range(len(message)):
        #converts letters to morse code
        tmessage += MORSE_CODE[message[letter]] + " "
    #prints message
    print(f"Your Translation: {tmessage}")
    time.sleep(1)
``` 

### Reflection

My main issues with this assignment was that I don't have a lot of experience with coding formats when it comes to manipulating text. One issue I ran into was in line 31 I didn't include "range" which caused an error because the length variable wasn't told to split itself by individual integers. To fix that all I did was make sure to put range out front and add some paranthesis around it. I changed a few variable names but I used large portions of Afton's work in this assignment. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook

## Morse Code Part 2

### Assignment Description

Write a script that translates messages into morse code onto an LED.

### Evidence 

![morse code part 2](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/b002d6fc-a607-4f67-98fd-6f237b4faa50)

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>   
![morse code 2 wiring](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/098a8463-931a-4979-abb2-a72b3cce1fcc)
</p>

</details>

### Code

 ```python
I used large portions of Afton's work in this assignment. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook
#type: ignore
#imports
import time 
import board 
import digitalio 
import pwmio
from digitalio import DigitalInOut,Direction,Pull

#morse code library
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'a----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

led = digitalio.DigitalInOut(board.GP0) #initialize green led 
led.direction = digitalio.Direction.OUTPUT

while True: 
    #lowercases letters
    message = input("Your Message: ").upper()
    #defins message
    tmessage = ""
    #exits code if "-q" is tpyed
    if "-Q" in message:
        break
    #for loop with message
    for letter in range(len(message)):
        #converts letters to morse code
        tmessage += MORSE_CODE[message[letter]] + " "
    for character in tmessage:
        if character == ".":
            led.value = True
            time.sleep(dot_time)
            led.value = False
            time.sleep(between_taps)
        if character == "-":
            led.value = True
            time.sleep(dash_time)
            led.value = False
            time.sleep(between_taps)
        if character == " ":
            time.sleep(between_letters)
            led.value = False
        if character == "/":    
            time.sleep(between_words)
            led.value = False
    #prints message
    print(f"Your Translation: {tmessage}")
    time.sleep(1)
```

### Reflection

My only issue with this assignment was some logic stuff in my "for character" loop. I originally would turn on the led for every single dot, dash, slash, or space. As a result the led would never turn off. So first I made sure to turn off the led after sleeping for the provided times. Even still, the led would never turn off. I realized that for the spaces or slashes I needed to not turn the led on at all and instead only sleep after turning th led off. The final bit was that my led wouldn't turn off after dots or dashes still because I didn't sleep after turning the led off. To fix this I added a time.sleep(between_taps) after turning the led off for dots and dashes and the translation works properly now. This is a continuation from the previous assignment which means I used large portions of Afton's work in this assignment. Here is a link to their notebook: https://github.com/Avanhoo/Engineering_4_Notebook

## Data Storage

### Assignment Description

Write code that puts your code into "code mode" and "data mode" which can read and write code to your pico while it's in "headless" mode.

### Evidence 

![ezgif com-optimize (3)](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/4534377f-86c3-4af5-8c6c-b8f4e03ea986)

### Wiring

<details>
<summary><b>Wiring Diagram</b></summary>

<p>
    
![data storage part 1](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/da0c9c99-1d67-478e-adc0-c82f9c41436d)

</p>

</details>

### Code

```python
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
```

### Data

|      |         |          |          |   |
|------|---------|----------|----------|---|
|7.609 |0.869095 |9.09079   |9.08121   |0  |
|8.725 |0.785298 |8.74602   |8.63589   |0  |
|9.744 |0.823606 |-0.169988 |-0.198719 |0  |
|10.764|0.3304   |6.06691   |5.82509   |0  |
|11.783|-5.3702  |7.47709   |7.2688    |0  |
|12.8  |-8.63828 |-3.98635  |-4.05338  |0  |
|13.822|-8.82981 |-4.05817  |-4.0462   |0  |
|14.842|-7.43639 |-7.38132  |-7.13233  |0  |
|15.859|-8.90882 |-0.23942  |0.00718261|0  |
|16.873|1.15879  |-0.248997 |-0.126893 |1  |
|17.888|1.13006  |1.1133    |1.86508   |1  |
|18.895|11.9375  |-5.26245  |-5.63595  |1  |
|19.913|-18.5551 |-0.0574608|0.215478  |0  |
|20.929|-4.29999 |-10.8936  |-10.3932  |0  |
|21.945|-0.605733|8.94713   |8.92798   |0  |
|23.051|0.754174 |7.82425   |7.95593   |0  |
|24.071|-4.00071 |8.4228    |8.31267   |0  |
|25.091|-2.22182 |8.71011   |8.52336   |0  |
|26.114|0.826    |8.67898   |8.75799   |0  |
|27.132|-9.15782 |-2.12366  |-2.229    |0  |
|28.153|-3.58173 |8.97826   |8.83939   |0  |
|29.175|0.921768 |8.95671   |9.11473   |0  |
|30.199|0.972046 |9.09557   |9.10754   |0  |
|31.218|0.931345 |9.05966   |9.07881   |0  |
|32.239|0.938527 |8.99741   |8.97586   |0  |
|33.258|0.909797 |9.12191   |9.11951   |0  |

### Reflection

This assignment was really tough for me for a couple reasons. First, I highly suggest reading the assignment with actual intent and not just skimming it. Second make sure your "while True" loop is in the "with open("/data.csv", "a") as datalog:" loop. I didn't do this at first and as a result the data file was never created. Third, make sure your boot.py code is in its own file rather than within your code for this assignment. Fourth and most importantly make sure when you go into headless mode that you don't have both your pico plugged in and a battery plugged in, or else your pico will be wiped.

## Data Analysis

### Assignment Description

Create graphs that relate to the data you collect with your pico in the prior assignment.

### Evidence 

![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/aff5fa7b-bbe7-40c1-926f-691e011bc289)

![image](https://github.com/nbednar2929/Engineering_4_Notebook/assets/91289646/d7b57739-7eea-41a4-bafb-8f6ef51da839)

[Link To Google Sheet](https://docs.google.com/spreadsheets/d/1_eP50iDxWyoMo7slHolbNCl_w958yNgELhV2aNQn0vQ/edit#gid=0)

### Wiring

No wiring was required for this assignment.

### Code

No code was required for this assignment. 

### Reflection

Hee hoo! Boy o' boy I love a good graph! Yippie! If you are looking to find some helpful advice on this assignment... Look somewhere else! This graph reminds of me of my youth, the good ol' days, before all these damn youngin libs took over. God bless America and come on down to buy a new Chevrolet at the giant American flag with Charlie Oball Chevrolet in beautiful Stanton!

&nbsp;

# Templates

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code

Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test
Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[Hyperlink text](http://www.turtle.com)        

### Test Image

![Turtle Picture](images/turtle.png)  

### Test GIF

![Turtle GIF](images/giphy.gif)  
