# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY


GPIO.setup(4, GPIO.OUT) # Connected to PWMA
GPIO.setup(17, GPIO.OUT) # Connected to AIN2
GPIO.setup(18, GPIO.OUT) # Connected to AIN1
GPIO.setup(27, GPIO.OUT) # Connected to STBY

def test():
    print("Hi")
    # Drive the motor clockwise
    GPIO.output(18, GPIO.HIGH) # Set AIN1
    GPIO.output(17, GPIO.LOW) # Set AIN2

    # Set the motor speed
    GPIO.output(4, GPIO.HIGH) # Set PWMA

    # Disable STBY (standby)
    GPIO.output(27, GPIO.HIGH)

    # Wait 1.1 seconds
    time.sleep(3.8)
    
    # Pause the motor
    GPIO.output(18, GPIO.LOW) # Set AIN1
    GPIO.output(17, GPIO.LOW) # Set AIN2
 
    # Set the motor speed
    GPIO.output(4, GPIO.LOW) # Set PWMA

    # Disable STBY (standby)
    GPIO.output(27, GPIO.LOW)

    # Wait 1.1 seconds
    time.sleep(1.1)
    
    # Drive the motor counterclockwise
    GPIO.output(18, GPIO.LOW) # Set AIN1
    GPIO.output(17, GPIO.HIGH) # Set AIN2
 
    # Set the motor speed
    GPIO.output(4, GPIO.HIGH) # Set PWMA

    # Disable STBY (standby)
    GPIO.output(27, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(3.8)

    # Reset all the GPIO pins by setting them to LOW
    GPIO.output(18, GPIO.LOW) # Set AIN1
    GPIO.output(17, GPIO.LOW) # Set AIN2
    GPIO.output(4, GPIO.LOW) # Set PWMA
    GPIO.output(27, GPIO.LOW) # Set STBY
    
test()
