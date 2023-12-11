from gpiozero import DistanceSensor
import time


import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(4, GPIO.OUT) # Connected to PWMA
GPIO.setup(17, GPIO.OUT) # Connected to AIN2
GPIO.setup(18, GPIO.OUT) # Connected to AIN1
GPIO.setup(27, GPIO.OUT) # Connected to STBY

ultrasonic = DistanceSensor(echo = 25, trigger = 20)





ultrasonic = DistanceSensor(echo = 25, trigger = 20)
while True:
    print(ultrasonic.distance)
    if ultrasonic.distance <= .3:
        print("short")
        time.sleep(5)
    
