import boto3
import json
import os
import cv2
import ssl
# Import required modules
import time
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(4, GPIO.OUT) # Connected to PWMA
GPIO.setup(17, GPIO.OUT) # Connected to AIN2
GPIO.setup(18, GPIO.OUT) # Connected to AIN1
GPIO.setup(27, GPIO.OUT) # Connected to STBY

ultrasonic = DistanceSensor(echo = 25, trigger = 20)


def take_photo(pic,  port=0, ramp_frames=30, x=1280, y=720):  
    camera = cv2.VideoCapture(0)
 #Camera Resolution
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    camera.set(3, x)
    camera.set(4, y)
 # Adjust camera lighting
    for i in range(ramp_frames):
        temp = camera.read()
    retval, im = camera.read()
 #Takes Photo
    cv2.imwrite("test.jpg",im)
    print("photo" + str(pic) + "taken")

#Removes Photo
    del(camera)

def upload_photo(pic,bucket):
    s3 = boto3.resource('s3')
    #s3.meta.client.upload_file('/Users/cjwong/Desktop/solving_school_shootings/'+str(pic), 'gun-rekognition', str(pic))
    s3.meta.client.upload_file(str(pic), bucket, str(pic))
    print("photo uploaded")

def detect_labels(pic, bucket):

    session = boto3.Session()
    client = session.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':pic}},
    MaxLabels=10)

    print('Detected labels for ' + pic)
    print()
    for label in response['Labels']:
        print("Label: " + label['Name'])
        print("Confidence: " + str(label['Confidence']))
        print("Instances:")
#This is where it checks to see if there is a Aluminum in the image
        if label['Name'] == "Steel":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Foil":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Aluminium":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Can":
            print("Parents:")
            motor()
            return
            
#This is where it checks to see if there is a Glass in the image
        elif label['Name'] == "Glass":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Jar":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Bottle":
            print("Parents:")
            motor()
            return
#This is where it checks to see if there is a Paper in the image
        elif label['Name'] == "Paper":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Newspaper":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Comics":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Publication":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Poster":
            print("Parents:")
            motor()
            return
#This is where it checks to see if there is a Plastic in the image
        elif label['Name'] == "Plastic":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Jug":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Water":
            print("Parents:")
            motor()
            return
        elif label['Name'] == "Bottle":
            print("Parents:")
            motor()
            return
        for parent in label['Parents']:
            print(" " + parent['Name'])

        print("Aliases:")
        for alias in label['Aliases']:
            print(" " + alias['Name'])

            print("Categories:")
        for category in label['Categories']:
            print(" " + category['Name'])
            print("----------")
            print()

    if "ImageProperties" in str(response):
        print("Background:")
        print(response["ImageProperties"]["Background"])
        print()
        print("Foreground:")
        print(response["ImageProperties"]["Foreground"])
        print()
        print("Quality:")
        print(response["ImageProperties"]["Quality"])
        print()

    return len(response['Labels'])


def main():
    pic = "test.jpg"
    take_photo(pic)
    bucket = 'recycledetect'
    upload_photo(pic,bucket)
    label_count = detect_labels(pic, bucket)
    print("Labels detected: " + str(label_count))




def motor():
    print("hello")
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


while True:
    print(ultrasonic.distance)
    if ultrasonic.distance <= .3:
        main()
        print("short")
        time.sleep(5)

