#type: ignore
import time
import board 
import digitalio 
import simpleio
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut,Direction,Pull

pwm = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 20, frequency=40)
my_servo = servo.Servo(pwm)

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
for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time forward.
    my_servo.angle = angle
    time.sleep(0.05)
Green.value = True #turn on green led for 5 seconds
time.sleep(5)
